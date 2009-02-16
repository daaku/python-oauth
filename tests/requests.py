# coding: utf-8

import unittest
import oauth
from oauth.signature_method.base import OAuthSignatureMethod


class TestRequests(unittest.TestCase):
    def test_url_with_query_string(self):
        request = oauth.OAuthRequest('http://daaku.org/?a=1')
        self.assertEqual(request.url, 'http://daaku.org/')
        self.assertEqual(request.params, {'a': '1'})

    def test_params_as_string(self):
        request = oauth.OAuthRequest('http://daaku.org/', params='a=1')
        self.assertEqual(request.url, 'http://daaku.org/')
        self.assertEqual(request.params, {'a': '1'})

    def test_auth_header(self):
        request = oauth.OAuthRequest(
            url='http://daaku.org/',
            http_method='POST',
            headers={'Authorization': 'OAuth oauth_version="1.0"'})
        self.assertEqual(request.url, 'http://daaku.org/')
        self.assertEqual(request.http_method, 'POST')
        self.assertEqual(request.params, {'oauth_version': '1.0'})

    def test_invalid_auth_header_bad_params(self):
        try:
            request = oauth.OAuthRequest(
                url='http://daaku.org/',
                headers={'Authorization': 'OAuth oauth_version'})
        except oauth.OAuthError:
            self.assert_(True)
        else:
            self.assert_(False, 'Was expecting OAuthError to be raised')

    def test_invalid_auth_header_no_data(self):
        try:
            request = oauth.OAuthRequest(
                url='http://daaku.org/',
                headers={'Authorization': 'OAuth '})
        except oauth.OAuthError:
            self.assert_(True)
        else:
            self.assert_(False, 'Was expecting OAuthError to be raised')

    def test_realm_in_auth_header(self):
        request = oauth.OAuthRequest(
            url='http://daaku.org/',
            headers={'Authorization': 'OAuth realm="daaku.org",oauth_version="1.0"'})
        self.assertEqual(request.params, {'oauth_version': '1.0'})

    def test_normalized_request_params(self):
        request = oauth.OAuthRequest(
            url='http://daaku.org/?a=1',
            http_method='POST',
            params={'b': '2'},
            headers={'Authorization': 'OAuth realm="daaku.org",oauth_version="1.0"'})
        self.assertEqual(
            request.normalized_request_params,
            'a=1&b=2&oauth_version=1.0'
        )

    def test_normalized_request_params_excludes_sig(self):
        request = oauth.OAuthRequest(
            url='http://daaku.org/?a=1',
            http_method='POST',
            params={'b': '2'},
            headers={'Authorization': 'OAuth realm="daaku.org",oauth_version="1.0",oauth_signature="abcd"'})
        self.assertEqual(
            request.normalized_request_params,
            'a=1&b=2&oauth_version=1.0')

    def test_incomplete_base_sig_method(self):
        request = oauth.OAuthRequest('http://daaku.org/')
        try:
            request.sign_request(OAuthSignatureMethod, {'oauth_token': 'myck'})
        except NotImplementedError:
            self.assert_(True)
        else:
            self.assert_(False, 'Expected NotImplementedError')

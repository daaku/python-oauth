# coding: utf-8

import unittest
import oauth
from oauth.signature_method.plaintext import OAuthSignatureMethod_PLAINTEXT


class TestPlaintext(unittest.TestCase):
    def test_validate_signature(self):
        auth_header = 'OAuth oauth_nonce="8982120766",oauth_timestamp="1234814886",oauth_consumer_key="myck",oauth_signature_method="PLAINTEXT",oauth_version="1.0",oauth_signature="%26"'
        request = oauth.OAuthRequest(
            'http://daaku.org/',
            headers={'Authorization': auth_header},
            timestamp_threshold=1234567890
        )
        request.validate_signature(OAuthSignatureMethod_PLAINTEXT, {'oauth_token': 'myck'})

    def test_missing_timestamp(self):
        request = oauth.OAuthRequest('http://daaku.org/')
        try:
            request.validate_signature(OAuthSignatureMethod_PLAINTEXT, {'oauth_token': 'myck'})
        except oauth.OAuthError, e:
            self.assert_(True)
        else:
            self.assert_(False, 'Expected OAuthError')

    def test_expired_timestamp(self):
        auth_header = 'OAuth oauth_nonce="8982120766",oauth_timestamp="1234814886",oauth_consumer_key="myck",oauth_signature_method="PLAINTEXT",oauth_version="1.0",oauth_signature="%26"'
        request = oauth.OAuthRequest(
            'http://daaku.org/',
            headers={'Authorization': auth_header},
        )
        try:
            request.validate_signature(OAuthSignatureMethod_PLAINTEXT, {'oauth_token': 'myck'})
        except oauth.OAuthError, e:
            self.assert_(True)
        else:
            self.assert_(False, 'Expected OAuthError')

    def test_invalid_sign_method(self):
        request = oauth.OAuthRequest(
            'http://daaku.org/',
            params={'oauth_timestamp': 1234814886, 'oauth_signature_method': 'blah'},
            timestamp_threshold=1234567890
        )
        try:
            request.validate_signature(OAuthSignatureMethod_PLAINTEXT, {'oauth_token': 'myck'})
        except oauth.OAuthError, e:
            self.assert_(True)
        else:
            self.assert_(False, 'Expected OAuthError')

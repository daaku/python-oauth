# coding: utf-8

import unittest
import oauth
from oauth.signature_method.hmac_sha1 import OAuthSignatureMethod_HMAC_SHA1


class TestHmacSha1(unittest.TestCase):
    def test_validate_signature(self):
        auth_header = 'OAuth oauth_nonce="3952607326",oauth_timestamp="1234814428",oauth_consumer_key="myck",oauth_signature_method="HMAC-SHA1",oauth_version="1.0",oauth_signature="ct4wwv2DUVu463wZEjXIgHu5pK8%3D"'
        request = oauth.OAuthRequest(
            'http://daaku.org/',
            headers={'Authorization': auth_header},
            timestamp_threshold=1234567890
        )
        consumer = {
            'oauth_token': 'myck',
            'oauth_token_secret': 'mycks',
        }
        request.validate_signature(OAuthSignatureMethod_HMAC_SHA1, consumer)

oauth
=====

A `python <http://python.org/>`_ implementation of the signature logic
associated with the `OAuth 1.0 <http://oauth.net/core/1.0/>`_ protocol. It is
not designed to handle the entire OAuth flow, and blissfully ignores the nonce.
Use it for generating and validating signatures.

The code is hosted
`here at github <https://github.com/nshah/python-oauth/tree/master>`_.
The latest code can be downloaded as a
`zip file <http://github.com/nshah/python-oauth/zipball/master>`_ or a
`tarball <http://github.com/nshah/python-oauth/tarball/master>`_.

Requires Python 2.6 or newer and `python-urlencoding
<http://code.daaku.org/python-urlencoding/>`_.

Can be installed using `pip <http://pip.openplans.org/>`_::

    pip install -r http://code.daaku.org/python-oauth/reqs

.. toctree::

************
OAuthRequest
************

This is the primary interface into the library.

.. autoclass:: oauth.OAuthRequest
    :members: validate_signature, sign_request, to_header, to_url, to_postdata

*****************
Signature Methods
*****************

This library supports the three types of `signature methods
<http://oauth.net/core/1.0/#signing_process>`_ defined in the OAuth
specification. If you intend to use RSA-SHA1 signatures, you will also need to
make sure you have the `tlslite <http://www.trevp.net/tlslite/>`_ module
available.

If you are using the PLAINTEXT or HMAC-SHA1 signature methods, then all you
need to do is use the provided implementations. But the RSA-SHA1 implementation
requires you to create a concrete implementation by inheriting from
OAuthSignatureMethod_RSA_SHA1 and provide a *public_cert* and a *private_cert*,
and use your class as the signature_method for signing and validating
requests.

.. autoclass:: oauth.signature_method.base.OAuthSignatureMethod
    :members:
.. autoclass:: oauth.signature_method.hmac_sha1.OAuthSignatureMethod_HMAC_SHA1
.. autoclass:: oauth.signature_method.rsa_sha1.OAuthSignatureMethod_RSA_SHA1
    :members:
.. autoclass:: oauth.signature_method.plaintext.OAuthSignatureMethod_PLAINTEXT

*****
Error
*****

.. autoclass:: oauth.OAuthError

from setuptools import setup, find_packages

setup(
    name='oauth',
    version='0.0.1',
    description='OAuth Signature Generation/Validation',
    author='Naitik Shah',
    author_email='n@daaku.org',
    url='https://code.daaku.org/python-oauth/',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools', 'setuptools_git', 'urlencoding'],
    extras_require = {
        'RSA': ['tlslite'],
    },
)

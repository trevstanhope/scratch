"""
Flask-ZMQ
----------

Adds ZMQ support to your Flask application.
"""
from setuptools import setup


setup(
    name='Flask-ZMQ',
    version='0.1.1',
    url='https://github.com/rebill/flask-zmq',
    license='BSD',
    author='Rebill',
    author_email='rebill@qq.com',
    description='Flask extension for ZMQ',
    long_description=__doc__,
    py_modules=['flask_zmq'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'pyzmq',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
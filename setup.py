from setuptools import setup
from os import path
import updog2


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='updog2',
    version=updog2.version,
    url='https://github.com/OBoladeras/updog2',
    # GitHub releases in format "updog-X.Y"
    download_url='https://github.com/OBoladeras/updog2/archive/updog-' + updog2.version + '.tar.gz',
    license='MIT',
    author='OBoladeras',
    author_email='oriolboladeras@gmail.com',
    description='Updog is a replacement for Python\'s SimpleHTTPServer. '
                'It allows uploading and downloading via HTTP/S, can set '
                'ad hoc SSL certificates and use http basic auth.'
                'The last version allows to generate a QR code to share the link.'
                'and also allows to display just image files in a more friendly way.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='HTTP server SimpleHTTPServer directory',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Communications :: File Sharing',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Security'
    ],
    packages=['updog2', 'updog2.utils'],
    entry_points={
        'console_scripts': 'updog2 = updog2.__main__:main'
    },
    include_package_data=True,
    install_requires=[
        'colorama',
        'flask',
        'flask_httpauth',
        'werkzeug',
        'pyopenssl',
        'qrcode'
    ],
)

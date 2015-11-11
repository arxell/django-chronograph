#!/usr/bin/python
from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

app_name = 'django-chronograph'
package_dir = 'chronograph'

for scheme in list(INSTALL_SCHEMES.values()):
    scheme['data'] = scheme['purelib']

packages = []
data_files = []

for dirpath, dirnames, filenames in os.walk(package_dir):
    # Ignore PEP 3147 cache dirs and those whose names start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.') or dirname == '__pycache__':
            del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(dirpath.split(os.sep)))
    elif filenames:
        data_files.append([os.sep.join(dirpath.split(os.sep)), [os.path.join(dirpath, f) for f in filenames]])

try:
    readme_filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pypi-readme.rst')
    long_description = open(readme_filename).read()
except IOError:
    long_description = None

description = 'Chronograph, a Django library for managing scheduled tasks (version mantained by Inoa)'
setup(
    name=app_name,
    version='0.1.22',
    description=description,
    long_description=long_description or description,
    url='https://github.com/joaofrancese/django-chronograph',
    author='Inoa Sistemas',
    author_email='django@inoa.com.br',
    packages=packages,
    install_requires=[
        "Django >= 1.7.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    data_files=data_files
)

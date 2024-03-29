import re

from setuptools import find_packages
from setuptools import setup

try:
    README = open('README.md').read()
except IOError:
    README = ''
try:
    CHANGELOG = open('CHANGELOG.md').read()
except IOError:
    CHANGELOG = ''


def load_reqs(filename):
    with open(filename) as reqs_file:
        return [
            re.sub('==', '>=', line) for line in reqs_file.readlines()
            if not re.match('\s*#', line)
        ]


requirements = load_reqs('requirements.txt')
test_requirements = load_reqs('requirements-test.txt')

setup(
    name='guillotina_linkintegrity',
    version='6.0.1.dev0',
    description='Link integrity support for guillotina',
    long_description=README + '\n\n' + CHANGELOG,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    author='Nathan Van Gheem',
    author_email='vangheem@gmail.com',
    url='https://github.com/guillotinaweb/guillotina_linkintegrity',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    tests_require=test_requirements,
    extras_require={
        'test': test_requirements
    },
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
    }
)

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

test_requirements = [
    'pytest>=4.1.1',
    'docker',
    'backoff',
    'psycopg2-binary',
    'pytest-asyncio>=0.8.0',
    'pytest-cov>=2.6.1',
    'coverage>=4.0.3',
    'pytest-docker-fixtures'
]


setup(
    name='guillotina_linkintegrity',
    version='1.0.7.dev0',
    description='Link integrity support for guillotina',
    long_description=README + '\n\n' + CHANGELOG,
    long_description_content_type='text/markdown',
    install_requires=[
        'guillotina>=4.4.5',
        'guillotina_rediscache',
        'lru-dict',
        'pypika',
        'lxml'
    ],
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

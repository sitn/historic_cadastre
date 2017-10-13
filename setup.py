# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='historic_cadastre',
    version='0.1',
    description='SITN, a sitn project',
    author='sitn',
    author_email='sitn@ne.ch',
    url='http://www.ne.ch/sitn',
    install_requires=[
        'c2c.template',
        'flake8',
        'geoalchemy2',
        'httplib2',
        'JSTools',
        'psycopg2',
        'pyramid',
        'sqlahelper',
        'SQLAlchemy',
        'psycopg2',
        'pyramid_multiauth',
        'pyramid_tm',
        'pyramid_debugtoolbar',
        'pyramid-mako',
        'pyyaml',
        'simplejson',
        'waitress',
        'zope.sqlalchemy',
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'paste.app_factory': [
            'main = historic_cadastre:main',
        ],
        'console_scripts': [
            'print_tpl = historic_cadastre.scripts.print_tpl:main',
        ],
    },
)
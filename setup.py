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
        'pyramid',
        'SQLAlchemy',
        'transaction',
        'pyramid_tm',
        'pyramid_debugtoolbar',
        'pyramid-mako',
        'zope.sqlalchemy',
        'waitress',
        'sqlahelper',
        'JSTools',
        'httplib2',
        'simplejson',
        'flake8',
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
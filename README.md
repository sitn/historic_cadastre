# historic_cadastre

## Installation

First, get the code:

    Drive:
    cd where_ever\historic_cadastre
    git init
    git remote add upstream https://github.com/sitn/historic_cadastre.git
    git fetch upstream
    git merge upstream/master

Next, run bootstrap (we are assuming that Python is in our path):

    python bootstrap-buildout.py --allow-site-packages

Finally, run buildout:

    buildout\bin\buildout.exe -c buildout.cfg

## Development

### Python code

When developping some Python code, you should run Flake8 on it, to be
sure that your code follows pep8

    buildout\bin\flake8 historic_cadastre\lib
    buildout\bin\flake8 historic_cadastre\views
    buildout\bin\flake8 historic_cadastre\models.py
    buildout\bin\flake8 historic_cadastre\__init__.py

(Do not run it on the whole package, because it contains a lot of external
libs).

It might also be good to check the McCabe complexity from time to time.

    buildout\bin\flake8 --max-complexity 10 historic_cadastre\lib
    buildout\bin\flake8 --max-complexity 10 historic_cadastre\views
    buildout\bin\flake8 --max-complexity 10 historic_cadastre\models.py
    buildout\bin\flake8 --max-complexity 10 historic_cadastre\__init__.py

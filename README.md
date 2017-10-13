# historic_cadastre project

## Building the application

### Requirements

historic_cadastre is meant to be built and used on Windows servers.

To do so, we need to be able to use "Linux" bash commands in a Windows cmd.

This can be achieved by installing some Cygwin components:

- make from the devel folder
- gettext-devel from the devel folder
- wget from the web folder

Moreover, these cannot directly be used in the Cygwin bash, but have to be added to the
path of the computer / server.

We recommand to add the following elements to the path (in the same order !)

1. Path to git (something like C:\Program Files (x86)\Git\cmd)
2. Path to Python (something like C:\Python27)
3. Path to Python scripts (something like C:\Python27\Scripts)
4. Path to Cygwin executables (something like C:\cygwin64\bin)

In the end, the following string should be added at the begin of the path:

    C:\Program Files\Git\cmd;C:\Python27;C:\Python27\Scripts;C:\cygwin64\bin;....

### Install an instance

First create an empty repository and initialize it with git and the project's repository:

    cd instance_folder
    git init
    git remote add upstream http://github.com/sitn/historic_cadastre.git
    git fetch upstream
    git merge upstream/master

Then create a specific make file for this instance and run the build process:

    make -f <instace_makefile>.mk build

Feel free to add project-specific things.

### Flake8

It is possible to check the Python code with Flake.

To do so, one might run the following exe, here typically for the admin.py file

    .build\venv\Scripts\flake8.exe historic_cadastre\views\entry.py
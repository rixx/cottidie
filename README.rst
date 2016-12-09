cottidie
########

Will collect all kinds of near-daily tasks and errands and functionality. May contain traces of latin.

Installation
============

:: 

    git clone https://github.com/rixx/cottidie.git
    cd cottidie
    mkvirtualenv cottidie  # or the venv manager of your choice
    pip install -r requirements.txt

Usage
=====

::

    workon cottidie  # or the venv manager of your choice
    python manage.py runserver

Development
===========

There are separate dev dependencies in `requirements/development.txt` which you probably
want to install. They are used for code styling (isort, pylama) and testing (pytest and its
addons).



.. reverse foreign key: pour le _set

The poll webpage
================

The idea is a web page which offers the implementation of a weighted
poll: participants might select *several* of the proposed choices, and
voters can *stress their preference* of a choice over another.

The poll  webpage is twofold, first there is creation page at shmoodle.net,
which when filled redirect to the newly created poll page (there is
one address for each created poll)

The creation page at http://shmoodle.net (why not!) offers this
short description and a form with the following fields:

- the **question**: for instance "Which theatre plays will we present
  to the public?"

- the **list of choices**: it is a string composed of string separated
  by commas. For example: "Phedre,Romeo and Juliet"

- if you want to administer it, you'll want to put your *name* and
  *password* to be able to modify later. The number of voting tokens
  to distribute might also be changed 

When the form is filled, the user is redirected to its, just created,
poll page, for instance http://shmoodle.net/4lph4b3t. The page is
composed of a table of the vote where each line is the vote of one
participants and each column is one of the possible choices of the
vote. The last line is the results: the number of participants so far
and the respectives sums of the vote for each choices. The standard
variation also shows to represent an indicator of the consensus as
well as the list of choices sorted by order of preferences.


the new's Web developer diary
-----------------------------

There are good chances that applications get designed around the SQL
models and the GET and POST HTTP paradigm instead of simple and clear
interfaces. Applications tightly coupled with SQL and HTTP are
difficult to reuse in other context: non interactive, API, command
line oriented, no SQL.

It is difficult to give a clear overview of user flow in urls, views
and templates. Example: a view indirectly returns a string containing
a tag *form*. Introspecting this tag, the action attributes indicates
the next url to which the form is sent. At this point, urls.py
indicates the views responsible for processing the form data. The view
generally ends with a *redirection* to the next url displayed to the
user. This is long... could this be simpler?

Unhelpful 'app not found' on ``manager.py sqlall``. The app is
indeed found but any exceptions or syntax error yields this
misleading error

I did not know a string instead of a class is acceptable for an
argument of the foreignKey field. This is important if there is a
need to declare a class after declaring the relation.

SQL is not so much fun to represent a list (and multivalued
fields). This impacts the design of many small models unneeded in
any high level languages embedding dictionaries and list as first
citizens. Note gor later: check the nosql new black.

Reverse *one* to *many* relation generate an attribute many\ *_set*
on the *one* object. It is surprising to use, in self's method an
attribute of self which is not declared in the class itself but
created by other classes.

The form fields and model fields are not similar, too bad. There is
no comma separated list.

Errors in the template_dir, in the regexp expressions, in the
patterns, in the template filename, are only caught at http get
request time. How to test a web app?

There is not much convention about where to put the templates in the
filesystem. There are not .py files hence use a parallel import
system. A hint would help he beginner: should it be in
project/templates, in project/templates/app or in
project/app/templates?

There is not much convention about how to split yet encapsulate the
code which sends a form and the code which process the form data. Can
we use callbacks? deferred? yield?

I would be lad to read some good hints on how to do The Right Thing
concerning the back button in the various situation of
post/get/authentication etc. I am sure people have gained experienced
and I am sure I will re-invent the wheel instead.

I confused the HttpRedirectResponse for a while. HttpRedirectResponse
is for *changing URL* and does not really accept a context. 

Smart templates are not compliant html, they can't be used by pure web
designer which are not programmers.


What is left todo
=================

- test test test, the configuration, the urls, the templates, the
  forms, the views, the models, the connection to the database. 

  How to test a Django app any web app?

- validate user input,

- i18n,

- memcache is no luxury: when a poll is created and when a when a
  ballot is casted, the user is redirected to a page which re-request
  the database about the exact same poll which would be better kept in memory for a short while instead of retrieved from the database,

- an admin role, secured password and https 

- presentation: css from meyers is desirable, longer text fields or
  text area

- going ajax might prove usefull and pave the way for xmpp interaction

http://en.wikipedia.org/wiki/Condorcet_method

http://en.wikipedia.org/wiki/Tactical_voting

http://en.wikipedia.org/wiki/Arrow%27s_impossibility_theorem


how to start a project?
=======================

::

  sudo aptitude install python-psycopg2 python-django{,-doc} postgresql
  sudo -s
  su postgres
  createuser jd
  exit # from being jd

  createdb shmoodle
  cd && django-admin startproject shmoodle
  cd shmoodle
  sed -i "s/# 'postgresql_psycopg2'/'postgresql_psycopg2' #/" settings.py
  # installed apps, template_dirs, template loaders and middleware classes
  python manage.py startapp poll
  mkdir poll/templates
  emacs poll/templates/{poll.html,vote.html} poll/forms.py

  emacs poll/views.py poll/models.py
  python manage.py sqlall | psql -d shmoodle  # syncdb
  python manage.py sqlclear poll | psql -d shmoodle




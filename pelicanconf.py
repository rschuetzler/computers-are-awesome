#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ryan Schuetzler'
SITENAME = 'Computers are Awesome'
SITEURL = ''

OUTPUT_PATH = 'docs/'

PATH = 'content/'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Enable needed plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['asciidoc_reader']

# Drafts for future dates
WITH_FUTURE_DATE = True

# Asciidoctor stuff
ASCIIDOC_CMD = 'asciidoctor'
ASCIIDOC_OPTIONS = ['-r', 'asciidoctor-bibtex']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

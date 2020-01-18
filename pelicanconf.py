#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'TCMG-316-GROUP1'
SITENAME = 'Aggie Life'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

IGNORE_FILES = ['_*.*']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Texas A&M University Events', 'https://calendar.tamu.edu/'),
         ('Texags', 'http://texags.com'),
         ('Aggie Traditions', 'https://www.tamu.edu/traditions/'),
         ('TAMU Student Life', 'https://www.tamu.edu/student-life/index.html'),)

# Social widget
SOCIAL = (('@TAMU', 'https://twitter.com/TAMU'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
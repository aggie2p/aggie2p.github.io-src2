#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Group-3'
SITENAME = 'TCMG 412-Group Three'
SITEURL = 'https://aggie2p.github.io'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME='pelican-chunk'

DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('About Class', '/pages/About.html'),
		 ('Our Team', '/pages/team.html'),
         ('What is Kanban', '/pages/Kanban.html'),
         ('TAMU TCMG', 'https://eahr.tamu.edu/academics/technology-management/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/tamu/'),
          ('@TAMU', 'https://twitter.com/TAMU'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URL = TRUE
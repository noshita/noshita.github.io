#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Koji NOSHITA'
SITENAME = 'Koji NOSHITA'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('生物測定学研究室', 'https://sites.google.com/a/ut-biomet.org/lbm/home'),
         ('数理生物学研究室', 'http://bio-math10.biology.kyushu-u.ac.jp/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/noshita'),)

# Formatting for URLs
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAGS_URL = 'tags/{slug}/'
TAG_SAVE_AS = "tag/{slug}/index.html"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Theme
THEME = './theme/pelican-bootstrap3'
# THEME = './theme/pure'
# THEME = './theme/html5-dopetrope'

# Mathematical Eqs.
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['render_math']
ALWAYS_MODIFIED = True


# Custamize
EVENTS_TITLE = '近況'
NEWS_TAG = 'news'
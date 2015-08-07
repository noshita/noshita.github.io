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

# Menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
			("Profile", "/pages/profile.html"),
			("Research", "/pages/research.html"),
			("Publications", "/pages/publications.html"),
			("Blog", "/category/blog/index.html")
			]

# Blogroll
LINKS = (('生物測定学研究室', 'https://sites.google.com/a/ut-biomet.org/lbm/home'),
         ('数理生物学研究室', 'http://bio-math10.biology.kyushu-u.ac.jp/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/noshita'),)

# Formatting for URLs
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

DISPLAY_CATEGORIES_ON_SIDEBAR = False
CATEGORY_URL = "category/{slug}/index.html"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

DISPLAY_TAGS_ON_SIDEBAR = True
TAGS_URL = 'tags/{slug}/index.html'
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
PLUGINS = ['render_math','tag_cloud']
# ALWAYS_MODIFIED = True
TAG_CLOUD_MAX_ITEMS = 10
TAG_CLOUD_SORTING = 'size' 

# Logo
SITELOGO = 'images/site_logo_sq.png'
SITELOGO_SIZE = 30
HIDE_SITENAME = True
FAVICON = 'images/site_logo_sq.png'

# About Me
ABOUT_ME = '<p>生物やその構造物の「かたち」を理論的に研究しています．</p>'
AVATAR = 'images/site_logo_sq.png'

# Custamize
EVENTS_TITLE = '近況'
NEWS_TAG = 'news'
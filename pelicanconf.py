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
			("Research", "/pages/research.html"),
			("Publications", "/pages/publications.html"),
			("Profile", "/pages/profile.html"),
			("Notes", ["/pages/notes.html", ("Morphometrics", "/pages/morphometrics.html"),("S&M", "/pages/sandm.html"),("Computational Biology", "/pages/compbio.html")]),
			("Blog", "/category/blog/index.html")
			]

# Blogroll
LINKS = (('生物測定学研究室', 'https://sites.google.com/a/ut-biomet.org/lbm/home'),
         ('数理生物学研究室', 'http://bio-math10.biology.kyushu-u.ac.jp/'),
         ('貝類学研究集会', 'http://www.molluscoida.org'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/noshita'),
		("RSS", "http://koji.noshita.net/feeds/all.atom.xml"),)
		# ('Mail', 'mailto:noshita@morphometrics.jp','envelope'),)

# Formatting for URLs
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

DISPLAY_CATEGORIES_ON_SIDEBAR = False
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

DISPLAY_TAGS_ON_SIDEBAR = True
TAGS_URL = 'tags/{slug}/'
TAG_SAVE_AS = "tag/{slug}.html"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Theme
THEME = './theme/pelican-bootstrap3'
# THEME = './theme/pure'
# THEME = './theme/html5-dopetrope'

# Extend Markdown
# MyEXTENSIONS_PATH = "./extensions/mdx_myextension.py"
# from extensions import mdx_myextension
import sys, os
MyEXTENSION_PATH = os.path.dirname(os.path.abspath(__file__)) + "/extensions"
sys.path.append(MyEXTENSION_PATH)
MD_EXTENSIONS = ['linkify', 'del_ins', 'fenced_code', 'codehilite(css_class=highlight)', 'tables', 'meta', 'footnotes', 'bibtex', 'myextension']

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
AVATAR = '/images/site_logo_sq.png'

# Custamize
ACTIVITIES_SLUG = 'activities'
NEWS_TAG = 'news'
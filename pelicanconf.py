#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import locale

AUTHOR = 'Koji NOSHITA'
SITENAME = 'Koji NOSHITA'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

# Locale
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'jp': '%Y年%m月%d日(%a)',
}

LOCALE = ('usa', 'jpn',  # On Windows
    'en_US', 'ja_JP'     # On Unix/Linux
    )

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
			("Blog", "/tag/blog.html")
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
ARTICLE_URL = "posts/{slug}.html"
ARTICLE_SAVE_AS = "posts/{slug}.html"

DISPLAY_CATEGORIES_ON_SIDEBAR = True
CATEGORY_URL = "category/{slug}.html"
CATEGORY_SAVE_AS = "category/{slug}.html"

DISPLAY_TAGS_ON_SIDEBAR = False
TAGS_URL = 'tags/{slug}.html'
TAG_SAVE_AS = "tag/{slug}.html"

MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Theme
THEME = './theme/pelican-bootstrap3'
# THEME = './theme/pure'
# THEME = './theme/html5-dopetrope'

# Extend Markdown
# MyEXTENSIONS_PATH = "./extensions"
# bibtex_ROOTPATH = "./content"
import sys, os
MyEXTENSION_PATH = os.path.dirname(os.path.abspath(__file__)) + "/extensions"
sys.path.append(MyEXTENSION_PATH)
bibtex_ROOTPATH = os.path.dirname(os.path.abspath(__file__)) + "/content"
# print(bibtex_ROOTPATH)
bibtex = "bibtex(root="+bibtex_ROOTPATH+")"
# Caution: To add bibtex into MD_EXTENSIONS, we need to write bibtex NOT 'bibtex'.
# 	Because new BibtexExtension class called if use 'bibtex' instead of bibtex.
MD_EXTENSIONS = ['del_ins', 'fenced_code', 'codehilite(css_class=highlight)', 'tables', 'meta', 'footnotes', bibtex, 'myextension']
# MD_EXTENSIONS = ['linkify', 'del_ins', 'fenced_code', 'codehilite(css_class=highlight)', 'tables', 'meta', 'footnotes']

# Mathematical Eqs.
# Caution: if 'render_math' plugin is enable, you must not use linkify.
# 	Because the linkify decorates domain-like strings with <a href= ></a> tags.
PLUGIN_PATHS = [os.path.dirname(os.path.abspath(__file__)) +'/pelican-plugins']
PLUGINS = ['tag_cloud', 'render_math', 'tipue_search']
# PLUGINS = ['tag_cloud', 'render_math']

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# ALWAYS_MODIFIED = True
TAG_CLOUD_MAX_ITEMS = 10
TAG_CLOUD_SORTING = 'size' 

# Logo
SITELOGO = 'images/site_logo_favi.png'
SITELOGO_SIZE = 30
HIDE_SITENAME = True
FAVICON = 'images/site_logo_favi.png'

# About Me
ABOUT_ME = '<p>生物やその構造物の「かたち」を理論的に研究しています．</p>'
AVATAR = '/images/site_logo_sq.png'

# Custamize
ACTIVITIES_SLUG = 'activities'
NEWS_CATEGORY = ['news','events']


# Static
STATIC_PATHS = ['images', 'materials', 'extras/CNAME', 'extras/custom.css']
EXTRA_PATH_METADATA = {'extras/CNAME': {'path': 'CNAME'},'extras/custom.css': {'path': 'static/custom.css'},}

CUSTOM_CSS = 'static/custom.css'

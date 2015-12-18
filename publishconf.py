#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://koji.noshita.net'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True


# Following items are often useful when publishing

import json
with open(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")), "r") as f:
	config = json.load(f) 
DISQUS_SITENAME = config["DISQUS_SITENAME"]
GOOGLE_ANALYTICS = config["GOOGLE_ANALYTICS"]
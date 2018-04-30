#!/usr/bin/env python
# This file is only used if you use `make publish` or
# explicitly specify it as your config file.
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://tech.chefclub.tv/'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = "feeds/%s.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
DISQUS_SITENAME = "tech-chefclub-tv"

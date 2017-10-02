#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Misc
SITEURL = 'http://xdays.me'
AUTHOR = u'xdays'
SITENAME = u'xdays'
KEYWORD = '架构，运维，开发, 生活随想'
STATIC_PATHS = ['wp-content']
EXTRA_PATH_METADATA = {
    'wp-content/static/robots.txt': {'path': 'robots.txt'},
    'wp-content/static/favicon.ico': {'path': 'favicon.ico'},
}
PATH = 'content'
OUTPUT_PATH = 'public'
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']
RELATIVE_URLS = True

# Time
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zh'

# Feed
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/rss.xml'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
MENUITEMS = (('首页', '/'), ('归档', 'archives.html'))
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Pagination
DEFAULT_PAGINATION = 20

# Output
DELETE_OUTPUT_DIRECTORY = True

# Theme
THEME = 'attila'
SOCIAL = (('twitter', 'https://twitter.com/easedays'),
          ('github', 'https://github.com/xdays'))

# Comment
DISQUS_SITENAME = 'xdays'

# Github
GITHUB_USER = 'xdays'
GITHUB_REPO_COUNT = 5 

# CacheMoment
CACHEMOMENT_REFER = True

# Goole Custom Search
GOOGLE_CSE_CODE = '008104676222079813428:xcoyettaqmw'

# Google Analyze
GOOGLE_ANALYTICS = 'UA-96220381-1'

# Google Adsense
GOOGLE_ADSENSE = True

PLUGINS = []

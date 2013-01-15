# -*- encoding: utf-8 -*-
# This is your configuration file.  Please write valid python!
# See http://posativ.org/acrylamid/conf.py.html

SITENAME = 'Groovematic'
WWW_ROOT = 'http://groovematic.com/'

AUTHOR = 'Isman Firmansyah'
EMAIL = 'isman.firmansyah@gmail.com'

FILTERS = [
    'markdown+extra+codehilite(css_class=highlight)',
]

VIEWS = {
    '/': {'view': 'articles'},
    '/about/': {'view': 'about'},
    '/:year/:month/:slug/': {'view': 'entry'},
    '/tag/:name/': {
        'view': 'tag',
        'pagination': '/tag/:name/:num'
    },
    '/atom.xml': {'filters': ['nohyphenate'], 'view': 'atom'},
    '/rss.xml': {'filters': ['nohyphenate'], 'view': 'rss'},
    # '/sitemap.xml': {'view': 'sitemap'},

}

THEME = 'theme'
ENGINE = 'acrylamid.templates.jinja2.Environment'
DATE_FORMAT = '%d.%m.%Y, %H:%M'

VIEWS_DIR = 'views/'

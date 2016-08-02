"""Development settings and globals."""

from __future__ import absolute_import

import os
from os.path import join, normpath

from analytics_dashboard.settings.dev import *
from analytics_dashboard.settings.logger import get_logger_config


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
    #  'analytics': {
        #  'ENGINE': 'django.db.backends.mysql',
        #  'NAME': 'reports_2_0',
        #  'USER': 'readonly001',
        #  'PASSWORD': 'meringues unfreehold sisterize morsing',
        #  'HOST': 'stage-edx-analytics-report-rds.edx.org',
        #  'PORT': '3306',
    #  }
}
########## END DATABASE CONFIGURATION

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
RJS_OPTIMIZATION_ENABLED = True

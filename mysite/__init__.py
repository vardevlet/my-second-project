#!/usr/bin/env python
from django.core.management import setup_environ
try:
    import config.settings as settings
except ImportError:
    import sys
    sys.stderr.write("Couldn't find the settings.py module.")
    sys.exit(1)
setup_environ(settings)
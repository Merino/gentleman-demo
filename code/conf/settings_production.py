# Production settings file.
# Brameda, 2011

from settings import *

# Debug settings
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Import any machine specific settings.
try:
    from settings_local import *
except ImportError:
    pass
# Staging settings file.
# Brameda, 2011

from settings import *

# Debug settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Import any machine specific settings.
try:
    from settings_local import *
except ImportError:
    pass
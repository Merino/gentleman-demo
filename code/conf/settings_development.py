# Development settings file.
# Brameda, 2011

from settings import *

# Debug settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG


# Installed Middleware
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Installed Apps
INSTALLED_APPS += (
    'debug_toolbar',
)

# Import any machine specific settings.
try:
    from settings_local import *
except ImportError:
    pass
from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^proofbasket/', include('proofbasket.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/password/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
        (r'^admin/password/done/$', 'django.contrib.auth.views.password_reset_done'),
        (r'^admin/password/reset/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views.password_reset_confirm'),
        (r'^admin/password/reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    (r'^admin/', include(admin.site.urls)),
    
    url(r'^admin_tools/', include('admin_tools.urls')),
)

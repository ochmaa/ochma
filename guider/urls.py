from django.conf.urls.defaults import *
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', name='login-page', kwargs = { 'template_name' : 'login.html', }),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout-page'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('guider.skul.urls')),
)

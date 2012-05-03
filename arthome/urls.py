from django.conf.urls import patterns, include, url
from arthomeapp import views
from django.conf import settings
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^add_artwork/$', views.upload_art),
    (r'^gallery/$', views.gallery),
    (r'^view_artwork/(\d+)$', views.view_artwork),
    (r'^fund_artwork/(\d+)$', views.fund_artwork),
    (r'^login/$', login),
    (r'^logout/$', logout),


)

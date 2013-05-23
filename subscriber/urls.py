from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freeswitch_gui.views.home', name='home'),
    # url(r'^freeswitch_gui/', include('freeswitch_gui.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^add/', 'subscriber.views.add'),
    url(r'^get/(?P<user_id>\d+)/', 'subscriber.views.getUser'),
    url(r'^$', 'subscriber.views.all'),
)

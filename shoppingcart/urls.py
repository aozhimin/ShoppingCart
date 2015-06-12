from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shoppingcart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('backend.urls', namespace='backend')),
    url(r'^cart/', include('fastcart.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

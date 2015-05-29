from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from backend import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shoppingcart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^products/(?<product_id>\d+)/add/$', views.add_product, name='add_product'),
    (r'cart/view/', views.view_cart),
)

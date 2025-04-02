from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.coffee_list, name='coffee_list'),
    path('add_to_cart/<int:coffee_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('generate_bill/', views.generate_bill, name='generate_bill'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
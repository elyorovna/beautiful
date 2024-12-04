

from django.urls import path

from blog.views import index, about, client, contact, products, detail, clients, banner

urlpatterns = [
    path('', index, name = 'index'),
    path('about/', about, name = 'about'),
    path('client/', client, name = 'client'),
    path('contact/', contact, name = 'contact'),
    path('products/', products, name = 'products'),
    path('detail/<int:id>/', detail, name = 'detail'),
    path('clients/<int:id>/', clients, name = 'clients'),
    path('banner/<int:id>/', banner, name = 'banner')


]












from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),
    path('milk/', views.milk, name='milk'),
    path('bread/', views.bread, name='bread'),
    path('bacaleya/', views.bacaleya, name='bacaleya'),

]
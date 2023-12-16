from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

from .views import ProductListView,ProductCreateView,ProductDeleteView,ProductEditView, CateoryListView

app_name = 'shop'

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    
    path('home/', ProductListView.as_view(), name='home'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(),name='product_delete'),
    path('product/<int:pk>/edit/', ProductEditView.as_view(),name='edit'),
    path('category-product-list/<int:cat_id>/', views.category_product_list,name='category-product-list'),
    path('category-list/', views.CateoryListView.as_view(),name='category-list'),
    
    # path('api/products/', views.get_products, name='get_products'),
# 
]
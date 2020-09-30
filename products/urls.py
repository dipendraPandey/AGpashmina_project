from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('<slug>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('<category>/<sub_category>/<search>/', views.product_filter_search_view, name='product-filter-search'),
    path('ajax/category_product/', views.product_filter_search_view, name='ajax_load_category_product'),
]

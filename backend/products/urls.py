from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_create_view, name='product-list-create'), 
    path('<int:pk>/', views.product_detail_view, name='product-detail'), 
    path('<int:pk>/delete/', views.product_delete_view, name='product-delete'), 
    path('<int:pk>/update/', views.product_update_view, name='product-update'), 

    # path('listmixin/', views.product_mixin_view), # List
    # path('<int:pk>/mixindetail/', views.product_mixin_view),  # Details
    # path('createmixin/', views.product_mixin_view), # List
]
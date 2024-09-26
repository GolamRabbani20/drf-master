from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_create_view), 
    path('<int:pk>/', views.product_detail_view), 
    path('<int:pk>/delete/', views.product_delete_view), 
    path('<int:pk>/update/', views.product_update_view), 

    # path('listmixin/', views.product_mixin_view), # List
    # path('<int:pk>/mixindetail/', views.product_mixin_view),  # Details
    # path('createmixin/', views.product_mixin_view), # List
]
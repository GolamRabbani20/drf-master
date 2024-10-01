from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlgoliaSearchListView.as_view(), name='algoliasearch'),
    path('drfsearch/', views.SearchListView.as_view(), name='drfsearch'),
   
]
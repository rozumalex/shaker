from django.urls import path
from django.views.decorators.cache import never_cache

from . import views


app_name = 'radio'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('library/', views.LibraryView.as_view(), name='library'),
]
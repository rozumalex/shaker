from django.urls import path

from . import views


app_name = 'radio'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('library/', views.LibraryView.as_view(), name='library'),
    path('bg/', views.get_background, name='background'),
    path('bg_list/', views.get_backgrounds_list, name='backgrounds_list')
]

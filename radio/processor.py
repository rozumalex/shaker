from django.db.models import Count
from django.contrib.auth.models import User
from .models import Track, SiteConfiguration
#
# def generate_extra_content():
#     extra_context = {
#         'new_tracks_list': Track.objects.order_by('-date_uploaded')[:5],
#         'active_users_list': User.objects.annotate(uploads=Count('user_uploaded')).order_by('-uploads')[:5],
#         'config': SiteConfiguration.objects.get(),
#     }
#     return extra_context

def generate_extra_content():
    return {
        'new_tracks_list': get_tracks(),
    }

def get_tracks():
    return Track.objects.order_by('-date_uploaded')[:5]

def get_users():
    return User.objects.annotate(uploads=Count('user_uploaded')).order_by('-uploads')[:5]

def get_config():
    return SiteConfiguration.objects.get()
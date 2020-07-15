from django.views import generic
from django.http import request
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models import QuerySet

from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3

from .forms import TrackUploadForm
from .models import Track


class IndexView(generic.edit.FormView):
    template_name = 'index.html'
    form_class = TrackUploadForm
    success_url = '/'
    # count_tracks = Track.objects.all().count()
    new_tracks_list = Track.objects.order_by('-date_uploaded')
    active_users_list = User.objects.annotate(uploads=Count('user_uploaded')).order_by('-uploads')[:5]
    extra_context = {
        'new_tracks_list': new_tracks_list,
        'active_users_list': active_users_list,
    }

    def form_valid(self, form):
        track = EasyID3(self.request._files['file'])
        # form.save()
        obj = form.save(commit=False)
        obj.user_uploaded = self.request.user
        obj.title = track['title'][0]
        obj.artist = track['artist'][0]
        obj.album = track['album'][0]
        obj.year = track['date'][0]
        obj.genre = track['genre'][0]
        obj.track_number = track['tracknumber'][0].split('/')[0]
        obj.save()

        return super().form_valid(form)

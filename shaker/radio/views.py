from django.views import generic
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import reverse
from django.db.models import Q
from django.http import JsonResponse

from mutagen.easyid3 import EasyID3

from .forms import TrackUploadForm
from .models import Track


class IndexView(generic.edit.FormMixin, generic.ListView):
    template_name = 'radio/index.html'
    model = Track
    form_class = TrackUploadForm
    context_object_name = 'new_tracks_list'
    ordering = ['-date_uploaded']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        kwargs['count_tracks'] = Track.objects.count()
        kwargs['active_users_list'] = User.objects.annotate(uploads=Count('user_uploaded')).order_by('-uploads')[:5]
        return super(IndexView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        form = self.get_form()
        if form.is_valid():
            data = self.form_valid(form)
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

    def form_valid(self, form):
        track = EasyID3(self.request._files['file'])
        obj = form.save(commit=False)
        obj.user_uploaded = self.request.user
        obj.title = track['title'][0]
        obj.artist = track['artist'][0]
        obj.album = track['album'][0]
        obj.year = track['date'][0]
        obj.genre = track['genre'][0]
        obj.track_number = track['tracknumber'][0].split('/')[0]
        obj.save()
        # return super().form_valid(form)
        return {'is_valid': True, 'artist': obj.artist, 'title': obj.title, 'user_uploaded': obj.user_uploaded.username}

    def get_success_url(self):
        return reverse('radio:index')


class LibraryView(generic.ListView):
    template_name = 'radio/library.html'
    model = Track
    context_object_name = 'tracks_list'
    ordering = ['-artist', '-title']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query == None:
            query = ''
        tracks_list = Track.objects.filter(
            Q(title__icontains=query) | Q(artist__icontains=query) | Q(album__icontains=query) | Q(year__icontains=query)
        )
        return tracks_list


from django.contrib import admin

from .models import Track


class TrackAdmin(admin.ModelAdmin):
    list_display = ('file', 'title', 'artist', 'album', 'year', 'genre', 'date_uploaded', 'user_uploaded')
    list_display_links = ('title',)
    list_filter = ('genre', 'artist', 'year', 'user_uploaded')
    search_fields = ('title', 'album', 'artist')


admin.site.register(Track, TrackAdmin)

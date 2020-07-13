from django.views import generic

from .forms import SongUploadForm


class IndexView(generic.edit.FormView):
    template_name = 'index.html'
    form_class = SongUploadForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

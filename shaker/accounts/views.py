from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(generic.ListView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'tracks_list'
    paginate_by = 15
    ordering = ['-artist', '-title']

    def get_queryset(self):
        user = self.request.user
        return user.user_uploaded.all()

    def get_context_data(self, **kwargs):
        user = self.request.user
        kwargs['count_tracks'] = user.user_uploaded.count()
        return super(ProfileView, self).get_context_data(**kwargs)

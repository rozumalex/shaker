from django.urls import path

from . import views


app_name = 'accounts'

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]

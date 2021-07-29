from django.urls import path

from accounts.views import LoginView
from accounts.views import RegistrationView

urlpatterns = [
    path('', LoginView.as_view(), name='Login_url'),
    path('register/', RegistrationView.as_view(),name='Registration_url')
]
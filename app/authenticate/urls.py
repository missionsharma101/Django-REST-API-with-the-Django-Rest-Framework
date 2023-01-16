from django.urls import path

from app.authenticate.views import *

urlpatterns = [
    path('', GetAuthView.as_view(), name="auth"),
    path('CreateView', UserCreateView.as_view(), name="CreateView"),

]

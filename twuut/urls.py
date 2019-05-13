from django.urls import path

from .views import feed

app_name = "twuut"

urlpatterns = [
    path("feed/", feed),
]
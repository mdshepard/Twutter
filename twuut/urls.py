from django.urls import path
from django.views.generic.base import TemplateView

from .views import feed


app_name = "twuut"

urlpatterns = [
    path("feed/", feed, name="feed"),
]
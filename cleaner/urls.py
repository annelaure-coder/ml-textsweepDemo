from django.urls import path

from . import views

app_name = "cleaner"

urlpatterns = [
    path("", views.home, name="home"),
    path("history/", views.history, name="history"),
    path("api/clean/", views.api_clean, name="api_clean"),
]

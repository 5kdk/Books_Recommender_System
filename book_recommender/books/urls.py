from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("index", views.index, name="index"),
    path("update", views.update_DB, name="update"),
]

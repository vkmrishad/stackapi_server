from django.urls import path
from . import views as view

urlpatterns = [
    path(r'search', view.SearchView .as_view()),
]

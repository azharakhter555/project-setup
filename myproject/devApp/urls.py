from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('', views.index, name='index'),  # Define a URL pattern for the index page
]
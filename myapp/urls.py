from django.urls import path
from .views import list_blobs

urlpatterns = [
    path('list-blobs/', list_blobs, name='list_blobs'),
]
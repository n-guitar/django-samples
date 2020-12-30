from django.urls import path
from .views import list_page, create_page

urlpatterns = [
    path('list/', list_page, name='list'),
    path('create/', create_page, name='create'),
]
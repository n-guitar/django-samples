from django.urls import path
from .views import list_page, create_page, update_page, delete_page

urlpatterns = [
    path('list/', list_page, name='list'),
    path('create/', create_page, name='create'),
    path('update/<int:pk>', update_page, name='update'),
    path('delete/<int:pk>', delete_page, name='delete'),
]
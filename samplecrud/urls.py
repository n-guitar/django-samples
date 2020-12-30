from django.urls import path
from .views import ListPage, CreatePage, UpdatePage, DeletePage

urlpatterns = [
    path('list/', ListPage.as_view(), name='list'),
    path('create/', CreatePage.as_view(), name='create'),
    path('update/<int:pk>', UpdatePage.as_view(), name='update'),
    path('delete/<int:pk>', DeletePage.as_view(), name='delete'),
]

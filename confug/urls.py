from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('samplecrud/', include('samplecrud.urls')),
    path('accounts/', include('accounts.urls')),
]

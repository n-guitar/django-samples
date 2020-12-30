from django.contrib import admin
from django.urls import path, include # include追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('samplecrud/', include('samplecrud.urls')), # 追加
]

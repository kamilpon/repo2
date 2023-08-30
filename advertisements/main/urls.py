from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_advertisements/', include('app_advertisements.urls'))

]

from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
]
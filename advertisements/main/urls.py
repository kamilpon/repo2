from django.urls  import path
from . import views

urlpatterns = [
    path('', views.page_1, name= 'page_1'),
]
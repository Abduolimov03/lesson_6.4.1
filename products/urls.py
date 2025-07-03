from django.urls import path
from .views import *

urlpatterns = [
    path('pods/', pods_list, name='pods'),
    path('pods/<int:pk>/', pods_detail, name='pods-detail'),
    path('create/', create_pods, name='create')
]
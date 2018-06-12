from django.urls import path
from . import views

urlpatterns= [
    path('', views.blogHome, name='blog' ),
    path('<int:blog_id>', views.blogDetail, name='post')
]
from django.urls import path
from . import views
urlpatterns =[
    path('',views.siteblog, name='siteblog'),
    path('post/create', views.create_post, name='post-create'),
    path('details/',views.details, name='details'),
]
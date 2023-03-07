from django.urls import path
from . import views
urlpatterns =[
    path('',views.siteblog, name='siteblog'),
    path('details/',views.details, name='details'),
]
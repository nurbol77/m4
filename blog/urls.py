from django.urls import path
from .import views

urlpatterns = [
    path('blog/',views.post_view,name='blog'),
]
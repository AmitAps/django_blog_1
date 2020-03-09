from django.urls import path

from . import views

##https://docs.djangoproject.com/en/3.0/intro/tutorial03/

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.post_detail, name='post_detail'),
    path('delete/', views.post_delete, name='post_delete'),
    path('update/', views.post_update, name='post_update'),

]

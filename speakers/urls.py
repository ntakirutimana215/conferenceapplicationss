from django.urls import path

from . import views
#important urls 
urlpatterns = [
    path('', views.speaker_list, name='speaker_list'),
    path('create/', views.speaker_create, name='speaker_create'),
    path('<int:pk>/', views.speaker_detail, name='speaker_detail'),
    path('<int:pk>/edit/', views.speaker_edit, name='speaker_edit'),
    path('<int:pk>/delete/', views.speaker_delete, name='speaker_delete'),
]
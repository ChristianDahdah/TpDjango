from django.urls import path
from disks import views

urlpatterns = [
    path('', views.acceuil),
    path('album/<int:id>/', views.album, name='album'),
    path('recherche/', views.recherche, name='recherche'),
]

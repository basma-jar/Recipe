from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('ajouter_note/<int:pk>/', views.ajouter_note, name='ajouter_note'),
    # ...
]
from django.urls import path
from .views import *

urlpatterns = [
    path('notesapi/', NotesApi.as_view()),
    path('notesapi/update/<id>/', NotesApi.as_view()),
    path('notesapi/delete/<id>/', NotesApi.as_view()),
    path('get_user/', get_notes),
]

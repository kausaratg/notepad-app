from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('note', views.note, name='note'),
    path('note_list', views.note_list, name='note_list'),
    path('stared', views.stared, name="stared"),
    path('note_detail/<str:pk>/', views.note_detail, name='note_detail'),
    path('update_note/<str:pk>', views.update_note, name="update_note"),
    path('delete_note/<str:pk>', views.delete_note, name="delete_note"),
    path('starred_notes/<str:pk>', views.starred_notes, name='starred_notes'),
    path('log_me_out', views.log_me_out, name="log_me_out"),
]

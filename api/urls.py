from django.urls import path
from . import views

urlpatterns = [


 path('allequipes/', views.equipe_list, name='equipe_list'),
    path('<int:equipe_id>/', views.detail_equipe, name='detail_equipe'),
    path('create_equipe/', views.create_equipe, name='create_equipe'),
    path('edit/<int:pk>', views.edit_equipe, name='edit_equipe'),
    path('delete/<int:equipe_id>', views.delete_equipe, name='delete_equipe'),]


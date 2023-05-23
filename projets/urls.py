'''from django.urls import path
from . import views

urlpatterns = [
   
   path('allprojects/', views.projet_list, name='projet_list'),
    path('<int:projet_id>/', views.single_projet, name='single_projet'),
    path('registration/', views.projet_regi, name='projet_regi'),
    path('edit/<int:pk>', views.edit_projet, name='edit_projet'),
    path('delete/<int:projet_id>', views.delete_projet, name='delete_projet'),]'''
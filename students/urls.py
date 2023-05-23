from django.urls import path
from . import views

urlpatterns = [
   
    #projet
     path('allprojects/', views.projet_list, name='projet_list'),
    path('<int:projet_id>/', views.single_projet, name='single_projet'),
    path('registration/', views.projet_regi, name='projet_regi'),
    path('edit/<int:pk>', views.edit_projet, name='edit_projet'),
    path('delete/<int:projet_id>', views.delete_projet, name='delete_projet'),
     path('projets/popular/', views.popular_projects, name='popular_projects'),
      #Client
    path('client_list/', views.client_list, name='client_list'),
    path('project_requests/', views.project_requests, name='project_requests'),
    path('approve_project_request/<int:request_id>/', views.approve_project_request, name='approve_project_request'),
    path('reject_project_request/<int:request_id>/', views.reject_project_request, name='reject_project_request'),


     path('inscription/client/', views.inscription_client, name='inscription_client'),
    path('inscription/personnel/', views.inscription_personnel, name='inscription_personnel'),
    path('connexion/client/', views.connexion_client, name='connexion_client'),
    path('connexion/personnel/', views.connexion_personnel, name='connexion_personnel'),


    path('demande-projet/', views.demande_projet, name='demande_projet'),

    path('reception-demande-projet/', views.reception_demande_projet, name='reception_demande_projet'),
    
]


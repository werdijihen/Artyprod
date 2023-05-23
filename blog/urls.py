from django.urls import path
from blog.views import article_list, article_detail, article_create, article_update, article_delete
from blog.views import demande_projet,demande_projet_list,modifier_demande_projet,supprimer_demande_projet
urlpatterns = [
    # ...
    path('articles/', article_list, name='article_list'),
    path('articles/create/', article_create, name='article_create'),
    path('articles/<int:pk>/', article_detail, name='article_detail'),
    path('articles/<int:pk>/update/', article_update, name='article_update'),
    path('articles/<int:pk>/delete/', article_delete, name='article_delete'),
    # ...
    #--------------------------------DEMANDE PROJET---------------------------------------
    path('demande_projet/', demande_projet, name='demande_projet'),
    path('demande_projet_list/', demande_projet_list, name='demande_projet_list'),
    path('demande_projet/<int:demande_projet_id>/edit/', modifier_demande_projet, name='modifier_demande_projet'),
    path('demande_projet/<int:demande_projet_id>/delete/', supprimer_demande_projet, name='supprimer_demande_projet'),


     
]

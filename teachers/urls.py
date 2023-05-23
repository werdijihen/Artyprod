from django.urls import path
from . import views

urlpatterns = [
    path('allpersonnels/', views.personnel_list, name='personnel_list'),
    path('<int:personnel_id>/', views.single_personnel, name='single_personnel'),
    path('registration/', views.create_personnel, name='create_personnel'),
    path('edit/<int:pk>', views.edit_personnel, name='edit_personnel'),
    path('delete/<int:personnel_id>', views.delete_personnel, name='delete_personnel'),


     path('personnels/<int:personnel_id>/payments/add/', views.add_payment, name='add_payment'),

    # URL pour la modification d'un paiement
    path('payments/<int:payment_id>/edit/', views.edit_payment, name='edit_payment'),
]


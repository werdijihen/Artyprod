from django.urls import path
from . import views

urlpatterns = [
    path('allservices/', views.service_list, name='service_list'),
    path('<int:service_id>/', views.single_service, name='single_service'),
    path('create_service/', views.create_service, name='create_service'),
    path('edit/<int:pk>', views.edit_service, name='edit_service'),
    path('delete/<int:service_id>', views.delete_service, name='delete_service'),
    path('search/',views.search,name='search')
]


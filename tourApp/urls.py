from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.tour_package_list, name='tour_package_list'),
    path('', views.package_list, name='package_list'),
    path('add/', views.add_package, name='add_package'),
    path('edit/<int:pk>/', views.edit_package, name='edit_package'),
    path('delete/<int:pk>/', views.delete_package, name='delete_package'),
]

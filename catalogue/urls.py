"""reservations.catalogue URL Configuration
"""
from django.urls import path
from . import views

app_name='catalogue'

urlpatterns = [
    path('artist/', views.artist.index, name='artist_index'),
    path('artist/<int:artist_id>', views.artist.show, name='artist_show'),
    path('type/', views.type.index, name='type_index'),
    path('type/<int:type_id>', views.type.show, name='type_show'),
    path('role/', views.role.index, name='role_index'),
    path('role/<int:role_id>', views.role.show, name='role_show'),
    path('locality/', views.locality.index, name='locality_index'),
    path('locality/<int:locality_id>', views.locality.show, name='locality_show'),
    path('location/', views.location.index, name='location_index'),
	path('location/<int:location_id>', views.location.show, name='location_show'),
    path('spectacle/', views.spectacle.index, name='spectacle_index'),
    path('spectacle/<int:spectacle_id>', views.spectacle.show, name='spectacle_show'),
    path('representation/', views.representation.representation_list, name='representation_list'),
    path('representation/<int:pk>/', views.representation.representation_detail, name='representation_detail'),
    path('representation/new/', views.representation.representation_create, name='representation_create'),
    path('representation/<int:pk>/edit/', views.representation.representation_update, name='representation_update'),
]

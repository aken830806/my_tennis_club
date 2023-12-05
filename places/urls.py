from django.urls import path
from . import views

urlpatterns = [
    path('places/', views.place_list, name='place_list'),
    path('booking/<int:place_id>/', views.booking, name='booking'),
    path('bookings/', views.booking_list, name='booking_list'),
]

from django.urls import path
from .views import doctor_list, book_appointment, appointment_confirmation

urlpatterns = [
    path('doctors/', doctor_list, name='doctor_list'),
    path('book/<int:doctor_id>/', book_appointment, name='book_appointment'),
    path('confirmation/<int:appointment_id>/', appointment_confirmation, name='appointment_confirmation'),
]

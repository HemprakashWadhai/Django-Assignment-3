from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Appointment
from accounts.models import User
from .google_calendar import create_calendar_event

@login_required
def doctor_list(request):
    doctors = User.objects.filter(user_type='Doctor')
    return render(request, 'doctor_list.html', {'doctors': doctors})

@login_required
def book_appointment(request, doctor_id):
    doctor = User.objects.get(id=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.doctor = doctor
            appointment.save()
            create_calendar_event(doctor, request.user, appointment)
            return redirect('appointment_confirmation', appointment_id=appointment.id)
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form, 'doctor': doctor})

@login_required
def appointment_confirmation(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    return render(request, 'appointment_confirmation.html', {'appointment': appointment})

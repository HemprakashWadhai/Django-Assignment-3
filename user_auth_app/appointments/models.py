from django.db import models
from accounts.models import User

class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')
    speciality = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def save(self, *args, **kwargs):
        # Automatically calculate the end time (45 minutes after the start time)
        import datetime
        self.end_time = (datetime.datetime.combine(datetime.date.today(), self.start_time) + datetime.timedelta(minutes=45)).time()
        super(Appointment, self).save(*args, **kwargs)

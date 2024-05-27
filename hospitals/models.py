from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class ServiceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='phamacies')
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='pharmacies')
    cover = models.ImageField(upload_to='pharmacy_cover')
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class PharmacyReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pharmacy_reviews')
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name='pharmacy_reviews')
    rating = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self) -> str:
        return self.user


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='clinic_cover/')

    def __str__(self) -> str:
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=100)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='fields')

    def __str__(self) -> str:
        return self.name


class Specialist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    cover = models.ImageField(upload_to='hospital_cover')
    rooms = models.PositiveIntegerField()
    acreage = models.PositiveIntegerField()
    clinic = models.ManyToManyField(Clinic, related_name='hospitals')
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hospitals', null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    lattitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class HospitalReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hospital_reviews')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.user


class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='doctors')
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='doctor_covers/')
    working_time = models.CharField(max_length=100)
    about = models.TextField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='doctors')
    specialist = models.ManyToManyField(Specialist, related_name='doctors')
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    call_price = models.PositiveIntegerField()
    message_price = models.PositiveIntegerField()
    videocall_price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.title


class DoctorReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_reviews')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reviews')
    review = models.CharField(max_length=250)
    rating = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.user


class ApointmentTypes(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Blood(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    phone = models.CharField(max_length=15)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='patients')
    blood = models.ForeignKey(Blood, on_delete=models.CASCADE, related_name='patients')
    profile_photo = models.ImageField(upload_to='patient_photos', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Apointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    time = models.DateField()
    price = models.PositiveIntegerField(null=True, blank=True)
    apointment_type = models.ForeignKey(ApointmentTypes, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')

    def __str__(self) -> str:
        return self.doctor
    

class FavoriteDoctor(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='favorite_doctors')
    doctors = models.ManyToManyField(Doctor, related_name='favorites')


class FavoriteHospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='favorite_hospitals')
    hospitals = models.ManyToManyField(Hospital, related_name='favorites')
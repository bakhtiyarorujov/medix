from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)


class ServiceType(models.Model):
    name = models.CharField(max_length=100)


class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='phamacies')
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='pharmacies')
    cover = models.ImageField(upload_to='pharmacy_cover')


class PharmacyReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pharmacy_reviews')
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name='pharmacy_reviews')
    rating = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=250, null=True, blank=True)


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='clinic_cover/')


class Doctor(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='doctor_covers/')
    working_time = models.CharField(max_length=100)
    about = models.TextField()
    
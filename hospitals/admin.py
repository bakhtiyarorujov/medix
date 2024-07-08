from django.contrib import admin
from . models import (
    City,
    ServiceType,
    Pharmacy,
    PharmacyReview,
    Clinic,
    Field,
    Specialist,
    Hospital,
    HospitalReview,
    Doctor,
    DoctorReview,
    ApointmentTypes,
    Gender,
    Blood,
    Patient,
    Apointment,
    FavoriteDoctor,
    FavoriteHospital
)
# Register your models here.


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'service_type', 'average_rating']
    list_display_links = ['name', 'city', 'service_type', 'average_rating']


@admin.register(PharmacyReview)
class PharmacyReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'pharmacy', 'rating', 'review']
    list_display_links = ['user', 'pharmacy', 'rating', 'review']


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ['name', 'clinic']
    list_display_links = ['name', 'clinic']


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'rooms', 'acreage', 'average_rating']
    list_display_links = ['name', 'rooms', 'acreage', 'average_rating']


@admin.register(HospitalReview)
class HospitalReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'hospital', 'rating', 'review']
    list_display_links = ['user', 'hospital', 'rating', 'review']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['title', 'field', 'hospital', 'average_rating']
    list_display_links = ['title', 'field', 'hospital', 'average_rating']


@admin.register(DoctorReview)
class DoctorReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'doctor', 'review', 'rating']
    list_display_links = ['user', 'doctor', 'review', 'rating']


@admin.register(ApointmentTypes)
class ApointmentTypesAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name'] 


@admin.register(Blood)
class BloodAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name'] 


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'birthday', 'user', 'gender', 'blood']
    list_display_links = ['first_name', 'last_name', 'phone', 'birthday', 'user', 'gender', 'blood']


@admin.register(Apointment)
class ApointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'time', 'price', 'apointment_type', 'patient']
    list_display_links = ['doctor', 'time', 'price', 'apointment_type', 'patient']


@admin.register(FavoriteHospital)
class FavoriteHospitalAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(FavoriteDoctor)
class FavoriteDoctorAdmin(admin.ModelAdmin):
    list_display = ['user']
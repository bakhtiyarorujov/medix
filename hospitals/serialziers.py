from rest_framework import serializers
from django.db.models import Min, Max
from .models import (
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

class ClinicGetSerialzier(serializers.ModelSerializer):
    number_of_hospitals = serializers.SerializerMethodField()
    min_price = serializers.SerializerMethodField()
    max_price = serializers.SerializerMethodField()
    class Meta:
        model = Clinic
        fields = (
            'id',
            'name',
            'cover',
            'number_of_hospitals',
            'min_price',
            'max_price',
        )
    
    def get_number_of_hospitals(self, obj):
        return obj.hospitals.count()

    def get_min_price(self, obj):
        # Calculate the minimum price for hospitals related to this clinic
        min_price = obj.hospitals.aggregate(min_price=Min('price'))
        return min_price['min_price']

    def get_max_price(self, obj):
        # Calculate the maximum price for hospitals related to this clinic
        max_price = obj.hospitals.aggregate(max_price=Max('price'))
        return max_price['max_price']
    

class HospitalGetSerializer(serializers.ModelSerializer):
    number_of_reviews = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()
    class Meta:
        model = Hospital
        fields = (
            'id',
            'name',
            'price',
            'cover',
            'rooms',
            'address',
            'acreage',
            'average_rating',
            'number_of_reviews',
            'is_favorite'
        )
    
    def get_number_of_reviews(self, obj):
        return obj.reviews.count()

    def get_is_favorite(self, obj):
        # Get the user from the context
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return FavoriteHospital.objects.filter(user=user, hospitals=obj).exists()

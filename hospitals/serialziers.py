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
            'description',
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


class HospitalDetailSerializer(serializers.ModelSerializer):
    number_of_reviews = serializers.SerializerMethodField()
    number_of_doctors = serializers.SerializerMethodField()
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
            'description',
            'acreage',
            'average_rating',
            'number_of_reviews',
            'number_of_doctors',
            'is_favorite'
        )
    
    def get_number_of_reviews(self, obj):
        return obj.reviews.count()

    def get_number_of_doctors(self, obj):
        return obj.doctors.count()

    def get_is_favorite(self, obj):
        # Get the user from the context
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return FavoriteHospital.objects.filter(user=user, hospitals=obj).exists()


class DoctorGetSerialzier(serializers.ModelSerializer):
    experience = serializers.SerializerMethodField(read_only=True)
    field = serializers.CharField(source='field.name')
    patients = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Doctor
        fields = (
            'id',
            'title',
            'cover',
            'experience',
            'field',
            'average_rating',
            'patients',
            'reviews',
        )
    
    def get_experience(self, obj):
        return obj.experience()
    
    def get_patients(self, obj):
        return obj.get_patients()
    
    def get_reviews(self, obj):
        return obj.get_review_count()
    

class SpecialistSerialzier(serializers.ModelSerializer):
    class Meta:
        model=Specialist
        fields = (
            'id',
            'name'
        )


class DoctorDetailSerialzier(serializers.ModelSerializer):
    experience = serializers.SerializerMethodField(read_only=True)
    field = serializers.CharField(source='field.name')
    patients = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)
    specialist = SpecialistSerialzier(many=True)
    class Meta:
        model = Doctor
        fields = (
            'id',
            'title',
            'cover',
            'experience',
            'field',
            'average_rating',
            'patients',
            'reviews',
            'specialist',
            'working_time',
            'about'
        )
    
    def get_experience(self, obj):
        return obj.experience()
    
    def get_patients(self, obj):
        return obj.get_patients()
    
    def get_reviews(self, obj):
        return obj.get_review_count()
    

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name'
        )


class PatientGetSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='gender.name')
    blood = serializers.CharField(source='blood.name')
    class Meta:
        model = Patient
        fields = (
            'id',
            'first_name',
            'last_name',
            'tag',
            'birthday',
            'phone',
            'gender',
            'blood',
            'profile_photo'
        )


class PatientCreateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'first_name',
            'last_name',
            'birthday',
            'tag',
            'phone',
            'gender',
            'blood',
            'profile_photo'
        ) 
    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return super().validate(attrs)


class BloodlistSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Blood
        fields = (
            'id',
            'name'
        )


class GenderlistSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = (
            'id',
            'name'
        )


class AppointmentTypeslistSerialzier(serializers.ModelSerializer):
    icon = serializers.ImageField(source='icon.icon')
    class Meta:
        model = ApointmentTypes
        fields = (
            'id',
            'name',
            'icon',
            'price'
        )


class AppointmentCreateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Apointment
        fields = (
            'doctor',
            'time',
            'apointment_type',
            'patient'
        ) 
    def validate(self, attrs):
        type = attrs['apointment_type']
        attrs['price'] = type.price
        attrs['user'] = self.context['request'].user
        return super().validate(attrs)


class AppointmentGetSerialzier(serializers.ModelSerializer):
    doctor = DoctorGetSerialzier()
    apointment_type = serializers.CharField(source='apointment_type.name')
    patient = PatientGetSerializer()
    class Meta:
        model = Apointment
        fields = (
            'id',
            'doctor',
            'time',
            'price',
            'apointment_type',
            'patient'
        )
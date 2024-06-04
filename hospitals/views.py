from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .filters import HospitalFilter
from django.shortcuts import get_object_or_404
from .serialziers import (
    ClinicGetSerialzier,
    HospitalGetSerializer,
    HospitalDetailSerializer,
    DoctorGetSerialzier,
    DoctorDetailSerialzier
)
from .models import (
    Clinic,
    Hospital,
    Doctor
)


class ClinicListView(ListAPIView):
    serializer_class = ClinicGetSerialzier
    permission_classes = [AllowAny]
    queryset = Clinic.objects.all()


class ClinicSearchView(ListAPIView):
    serializer_class = ClinicGetSerialzier
    permission_classes = [AllowAny]
    queryset = Clinic.objects.all()

    def get_queryset(self):
        keyword = self.kwargs.get('keyword')
        queryset = Clinic.objects.filter(name__icontains=keyword)[:10]
        return queryset


class HospitalListByClinicView(ListAPIView):
    serializer_class = HospitalGetSerializer
    permission_classes = [AllowAny]
    queryset = Hospital.objects.all()

    def get_queryset(self):
        clinic_id = self.kwargs.get('clinic_id')
        clinic = get_object_or_404(Clinic, id=clinic_id)
        queryset = Hospital.objects.filter(clinic=clinic)
        return queryset
    

class HospitalSearchView(ListAPIView):
    serializer_class = HospitalGetSerializer
    permission_classes = [AllowAny]
    queryset = Hospital.objects.all()

    def get_queryset(self):
        keyword = self.kwargs.get('keyword')
        queryset = Hospital.objects.filter(name__icontains=keyword)
        return queryset


class HospitalFilterListView(ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalGetSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = HospitalFilter


class HospitalDetailView(RetrieveAPIView):
    serializer_class = HospitalDetailSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        id = self.kwargs.get('hospital_id')
        hospital = get_object_or_404(Hospital, id=id)
        return hospital


class DoctorListView(ListAPIView):
    serializer_class = DoctorGetSerialzier
    permission_classes = [AllowAny]

    def get_queryset(self):
        id = self.kwargs.get('hospital_id')
        hospital = get_object_or_404(Hospital, id=id)
        queryset = hospital.doctors.all()
        return queryset


class DoctorDetailView(RetrieveAPIView):
    serializer_class = DoctorDetailSerialzier
    permission_classes = [AllowAny]

    def get_object(self):
        id = self.kwargs.get('doctor_id')
        doctor = get_object_or_404(Doctor, id=id)
        return doctor
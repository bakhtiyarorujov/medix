from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .filters import HospitalFilter
from django.shortcuts import get_object_or_404
from .serialziers import (
    ClinicGetSerialzier,
    HospitalGetSerializer,
    HospitalDetailSerializer,
    DoctorGetSerialzier,
    DoctorDetailSerialzier,
    CitySerializer,
    PatientGetSerializer,
    PatientCreateSerialzier,
    AppointmentCreateSerialzier,
    BloodlistSerialzier,
    GenderlistSerialzier,
    AppointmentTypeslistSerialzier,
    AppointmentGetSerialzier
)
from .models import (
    Clinic,
    Hospital,
    Doctor,
    City,
    Patient,
    Blood,
    Gender,
    ApointmentTypes,
    Apointment
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


class DoctorSearchView(ListAPIView):
    serializer_class = DoctorGetSerialzier
    permission_classes = [AllowAny]

    def get_queryset(self):
        keyword = self.kwargs.get('keyword')
        queryset = Doctor.objects.filter(title__icontains=keyword)
        return queryset


class DoctorDetailView(RetrieveAPIView):
    serializer_class = DoctorDetailSerialzier
    permission_classes = [AllowAny]

    def get_object(self):
        id = self.kwargs.get('doctor_id')
        doctor = get_object_or_404(Doctor, id=id)
        return doctor
    

class CityListView(ListAPIView):
    serializer_class = CitySerializer
    permission_classes = [AllowAny]
    queryset = City.objects.all()


class PatientListView(ListAPIView):
    serializer_class = PatientGetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        patients = user.patients.all()
        return patients


class PatientCreateView(CreateAPIView):
    serializer_class = PatientCreateSerialzier
    permission_classes = [IsAuthenticated]


class PatientDetailView(RetrieveAPIView):
    serializer_class = PatientGetSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        id = self.kwargs.get('patient_id')
        patient = get_object_or_404(Patient, id=id)
        return patient


class BloodListView(ListAPIView):
    serializer_class = BloodlistSerialzier
    permission_classes = [AllowAny]
    queryset = Blood.objects.all()


class GenderListView(ListAPIView):
    serializer_class = GenderlistSerialzier
    permission_classes = [AllowAny]
    queryset = Gender.objects.all()


class ApointmentTypesListView(ListAPIView):
    serializer_class = AppointmentTypeslistSerialzier
    permission_classes = [AllowAny]
    queryset = ApointmentTypes.objects.all()

    def get_queryset(self):
        id = self.kwargs.get('doctor_id')
        doctor = get_object_or_404(Doctor, id=id)
        queryset = doctor.hospital.appointmenttypes.all()
        return queryset


class AppointmentCreateView(CreateAPIView):
    serializer_class = AppointmentCreateSerialzier
    permission_classes = [IsAuthenticated]


class ApointmentListView(ListAPIView):
    serializer_class = AppointmentGetSerialzier
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = user.appointments.all()
        return queryset
    
class ApointmentDetailView(RetrieveAPIView):
    serializer_class = AppointmentGetSerialzier
    permission_classes = [IsAuthenticated]

    def get_object(self):
        id = self.kwargs.get('id')
        apointment = get_object_or_404(Apointment, id=id)
        return apointment
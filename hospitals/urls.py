from django.urls import path
from .views import (
    ClinicListView,
    ClinicSearchView,
    HospitalListByClinicView,
    HospitalSearchView,
    HospitalFilterListView,
    HospitalDetailView,
    DoctorListView,
    DoctorDetailView,
    DoctorSearchView,
    CityListView
)
urlpatterns = [
    path('clinic/list', ClinicListView.as_view(), name='clinic_list'),
    path('clinic/search/<str:keyword>', ClinicSearchView.as_view(), name='clinic_search'),
    path('hospital/list/<int:clinic_id>', HospitalListByClinicView.as_view(), name='hospital_list_by_clinic'),
    path('hospital/search/<str:keyword>', HospitalSearchView.as_view(), name='hospital_search'),
    path('hospital/city/list', CityListView.as_view(), name='hospital_city_list'),
    path('hospital/filter-list', HospitalFilterListView.as_view(), name='hospital_list_by_filter'),
    path('hospital/detail/<int:hospital_id>', HospitalDetailView.as_view(), name='hospital_detail'),
    path('doctor/list/<int:hospital_id>', DoctorListView.as_view(), name='doctor_list_by_hospital'),
    path('doctor/detail/<int:doctor_id>', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctor/search/<str:keyword>', DoctorSearchView.as_view(), name='doctor_search'),
]

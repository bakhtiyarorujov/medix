from django.urls import path
from .views import (
    ClinicListView,
    ClinicSearchView,
    HospitalListByClinicView,
    HospitalSearchView,
    HospitalFilterListView
)
urlpatterns = [
    path('clinic/list', ClinicListView.as_view(), name='clinic_list'),
    path('clinic/search/<str:keyword>', ClinicSearchView.as_view(), name='clinic_search'),
    path('hospital/list/<int:clinic_id>', HospitalListByClinicView.as_view(), name='hospital_list_by_clinic'),
    path('hospital/search/<str:keyword>', HospitalSearchView.as_view(), name='hospital_search'),
    path('hospital/filter-list', HospitalFilterListView.as_view(), name='hospital_list_by_filter'),
]

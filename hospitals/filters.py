from django_filters import rest_framework as filters
from .models import Hospital
from geopy.distance import geodesic
from django.db.models import QuerySet

class HospitalFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    city = filters.CharFilter(field_name="city__name", lookup_expr='icontains')

    class Meta:
        model = Hospital
        fields = ['min_price', 'max_price', 'city']

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        # Custom distance filtering
        request = self.request
        user_latitude = request.query_params.get('latitude')
        user_longitude = request.query_params.get('longitude')
        max_distance = request.query_params.get('distance')

        if user_latitude and user_longitude and max_distance:
            user_location = (float(user_latitude), float(user_longitude))
            max_distance = float(max_distance)

            # Create a list to hold hospital ids that are within the distance
            nearby_hospital_ids = []
            for hospital in queryset:
                if hospital.latitude and hospital.longitude:  # Ensure we have the coordinates
                    hospital_location = (hospital.latitude, hospital.longitude)
                    distance = geodesic(user_location, hospital_location).km
                    if distance <= max_distance:
                        nearby_hospital_ids.append(hospital.id)

            queryset = queryset.filter(id__in=nearby_hospital_ids)

        return queryset

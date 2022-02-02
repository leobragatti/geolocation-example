
from django.db.models import Q

from django.contrib.gis.geos.point import Point
from django.contrib.gis.measure import D

from rest_framework import viewsets

from .serializers import TraderSerializer
from .models import Trader


# Create your views here.

class TraderViewSet(viewsets.ModelViewSet):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Trader.objects.all()
        filters = self.request.query_params
        latitude = filters.get('lat')
        longitude = filters.get('lng')
        if longitude and longitude:
            point = Point(float(longitude), float(latitude))
            query = Q(address__distance_lte=(point, D(km=5))) | Q(coverage_area__covers=point)
            queryset = queryset.filter(query)

        return queryset
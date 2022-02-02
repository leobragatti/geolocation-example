import json

from rest_framework import serializers


class GeoJSONField(serializers.Field):
    def to_representation(self, value):
        return json.loads(value.geojson)

    def to_internal_value(self, data):
        pass
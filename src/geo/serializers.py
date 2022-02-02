from rest_framework import serializers

from .models import Trader

from .fields import GeoJSONField

class TraderSerializer(serializers.ModelSerializer):
    address = GeoJSONField()
    coverage_area = GeoJSONField()

    class Meta:
        model = Trader
        fields = '__all__'

    def snake_case_to_camel(self, content):
        components = content.split('_')
        words = ''.join([item.title() for item in components[1:]])
        return f'{components[0]}{words}'

    def to_representation(self, value):
        data = super().to_representation(value)
        converted = {self.snake_case_to_camel(key):value for key, value in data.items() }
        return converted

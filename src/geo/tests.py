import json

from django.test import TestCase

from rest_framework.test import APIRequestFactory, APIClient

from geo.models import Trader
from geo.serializers import TraderSerializer

# Create your tests here.
class TraderTestCase(TestCase):
    sample = {
        "id": 1,
        "tradingName": "Adega Osasco",
        "ownerName": "Ze da Ambev",
        "document": "02.453.716/000170",
        "coverageArea": {
            "type": "MultiPolygon",
            "coordinates": [
            [
                [
                    [
                        -43.36556,
                        -22.99669
                    ],
                    [
                        -43.36539,
                        -23.01928
                    ],
                    [
                        -43.26583,
                        -23.01802
                    ],
                    [
                        -43.25724,
                        -23.00649
                    ],
                    [
                        -43.23355,
                        -23.00127
                    ],
                    [
                        -43.2381,
                        -22.99716
                    ],
                    [
                        -43.23866,
                        -22.99649
                    ],
                    [
                        -43.24063,
                        -22.99756
                    ],
                    [
                        -43.24634,
                        -22.99736
                    ],
                    [
                        -43.24677,
                        -22.99606
                    ],
                    [
                        -43.24067,
                        -22.99381
                    ],
                    [
                        -43.24886,
                        -22.99121
                    ],
                    [
                        -43.25617,
                        -22.99456
                    ],
                    [
                        -43.25625,
                        -22.99203
                    ],
                    [
                        -43.25346,
                        -22.99065
                    ],
                    [
                        -43.29599,
                        -22.98283
                    ],
                    [
                        -43.3262,
                        -22.96481
                    ],
                    [
                        -43.33427,
                        -22.96402
                    ],
                    [
                        -43.33616,
                        -22.96829
                    ],
                    [
                        -43.342,
                        -22.98157
                    ],
                    [
                        -43.34817,
                        -22.97967
                    ],
                    [
                        -43.35142,
                        -22.98062
                    ],
                    [
                        -43.3573,
                        -22.98084
                    ],
                    [
                        -43.36522,
                        -22.98032
                    ],
                    [
                        -43.36696,
                        -22.98422
                    ],
                    [
                        -43.36717,
                        -22.98855
                    ],
                    [
                        -43.36636,
                        -22.99351
                    ],
                    [
                        -43.36556,
                        -22.99669
                    ]
                ]
            ]
            ]
        },
        "address": {
            "type": "Point",
            "coordinates": [
            -43.297337,
            -23.013538
            ]
        }
    }
    def test_serializer(self):
        serializer = TraderSerializer(Trader.objects.first())
        self.assertDictEqual(serializer.data, self.sample)

    def test_get_by_id(self):
        factory = APIClient()
        request = factory.get('/api/traders/1/', format='json')
        result = request.json()
        self.assertEqual(result, self.sample)


    def test_get_availables_area(self):
        coordinates = {
            'lat': -23.5868895,
            'lng': -46.6275977
        }
        factory = APIClient()
        request = factory.get('/api/traders/', coordinates, format='json')
        result = request.json()
        ids = [item.get('id') for item in result]
        self.assertIn(13, ids)
        self.assertIn(40, ids)
        self.assertIn(41, ids)
        self.assertIn(48, ids)
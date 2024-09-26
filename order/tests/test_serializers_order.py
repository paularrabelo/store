from django.test import TestCase

from order.factories import OrderFactory, ProductFactory
from order.serializers import OrderSerializer

class TestOrderSerializer(TestCase):
    def setUp(self) -> None:
        self.product_test = ProductFactory()

        self.order = OrderFactory(product=(self.product_test))
        self.order_serializer = OrderSerializer(self.order)

    def test_serializer(self):
        serializer_data = self.order_serializer.data
        self.assertEqual(
            serializer_data['product'][0]['title'], self.product_test.title)
from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer

class TestProductSerializer(TestCase):
    def test_product(self) -> None:
        self.category = CategoryFactory(title='Carro')
        self.product_test = ProductFactory(title='Fox', price=30000, category=[self.category])
        self.product_serializer = ProductSerializer(self.product_test)

    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data['price', 30000])
        self.assertEqual(serializer_data['title'], 'Fox')
        self.assertEqual(serializer_data['category'][0]['title'], 'Carro')
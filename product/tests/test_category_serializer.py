from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import CategorySerializer

class TestCategorySerializer(TestCase):
    def test_category(self) -> None:
        self.category = CategoryFactory(title='Test')
        self.category_serializer = CategorySerializer(self.category)

    def test_category_serializer(self):
        serializer_data = self.category_serializer.data

        self.assertEqual(serializer_data['title', 'Test'])
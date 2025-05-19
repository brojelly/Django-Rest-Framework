from django.test import TestCase
from .models import Restaurant

class RestaurantModelTest(TestCase):
    def test_create_restaurant(self):
        restaurant = Restaurant.objects.create(
            name='곱창이랑 곱창전골',
            address='서울시 곱창구',
            contact='010-1234-5678',
            open_time='11:00',
            close_time='22:00',
            last_order='21:30',
            regular_holiday='MON'
        )
        self.assertEqual(restaurant.name, '곱창이랑 곱창전골')
        self.assertEqual(restaurant.regular_holiday, 'MON')

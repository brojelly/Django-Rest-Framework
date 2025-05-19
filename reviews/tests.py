from django.test import TestCase
from users.models import User
from restaurants.models import Restaurant
from .models import Review

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', nickname='testuser', password='pass1234')
        self.restaurant = Restaurant.objects.create(
            name='곱창이네',
            address='서울 강남구',
            contact='02-0000-0000'
        )

    def test_create_review(self):
        review = Review.objects.create(
            user=self.user,
            restaurant=self.restaurant,
            title='최고였어요',
            comment='곱창이 아주 쫄깃하고 맛있었어요!'
        )
        self.assertEqual(review.title, '최고였어요')
        self.assertEqual(review.restaurant.name, '곱창이네')

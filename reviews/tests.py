from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from restaurants.models import Restaurant
from .models import Review

User = get_user_model()

# ✅ 1. 모델 테스트
class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com', nickname='testuser', password='pass1234'
        )
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


# ✅ 2. API 테스트
class ReviewAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="reviewer@example.com", nickname="reviewer", password="test1234"
        )
        self.restaurant = Restaurant.objects.create(name="테스트식당", address="서울")
        self.client.force_login(self.user)  # 🔐 로그인 확실하게

    def test_get_review_list(self):
        response = self.client.get(f"/reviews/restaurants/{self.restaurant.id}/reviews")
        self.assertEqual(response.status_code, 200)

    def test_post_review(self):
        data = {"title": "맛있어요", "comment": "또 가고 싶어요"}
        response = self.client.post(
            f"/reviews/restaurants/{self.restaurant.id}/reviews",
            data,
            format="json"  # ✅ 필수
        )
        self.assertEqual(response.status_code, 201)

    def test_get_review_detail(self):
        review = Review.objects.create(
            user=self.user, restaurant=self.restaurant,
            title="굿", comment="맛있다!"
        )
        response = self.client.get(f"/reviews/reviews/{review.id}")
        self.assertEqual(response.status_code, 200)

    def test_update_review(self):
        review = Review.objects.create(
            user=self.user, restaurant=self.restaurant,
            title="굿", comment="맛있다!"
        )
        data = {"title": "수정된 제목", "comment": "수정된 내용"}
        response = self.client.put(
            f"/reviews/reviews/{review.id}",
            data,
            content_type="application/json"  # 🔧 PUT/PATCH 요청에 필수!
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_review(self):
        review = Review.objects.create(
            user=self.user, restaurant=self.restaurant,
            title="굿", comment="맛있다!"
        )
        response = self.client.delete(f"/reviews/reviews/{review.id}")
        self.assertEqual(response.status_code, 204)


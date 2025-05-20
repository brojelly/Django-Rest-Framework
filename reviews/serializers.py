from rest_framework import serializers
from .models import Review
from users.serializers import UserDetailSerializer
from restaurants.serializers import RestaurantSerializer  # 필요 시 작성되어 있어야 함


# ✅ 리뷰 목록/작성용
class ReviewSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'restaurant', 'title', 'comment']
        read_only_fields = ['id', 'restaurant']


# ✅ 리뷰 상세/수정용
class ReviewDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'restaurant', 'title', 'comment']
        read_only_fields = ['id']

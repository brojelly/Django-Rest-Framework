# reviews/views.py
from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        restaurant_id = self.kwargs["restaurant_id"]
        return Review.objects.filter(restaurant__id=restaurant_id).order_by("-id")

    def perform_create(self, serializer):
        restaurant_id = self.kwargs["restaurant_id"]
        serializer.save(user=self.request.user, restaurant_id=restaurant_id)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def get_object(self):
        review_id = self.kwargs["review_id"]
        return self.get_queryset().get(id=review_id)


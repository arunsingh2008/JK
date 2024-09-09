


from django.urls import path
from .views import get_reviews_by_book_id

urlpatterns = [
    path('reviews/<int:book_id>/', get_reviews_by_book_id, name='get_reviews_by_book_id'),
]



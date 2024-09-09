


from django.http import JsonResponse
from .models import Review


def get_reviews_by_book_id(request, book_id):
    reviews = Review.objects.filter(book_id=book_id).values()
    return JsonResponse(list(reviews), safe=False)



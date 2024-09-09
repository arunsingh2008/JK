


from django.db import models


class Review(models.Model):
    book_id = models.IntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review_text



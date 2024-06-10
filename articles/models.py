from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    body = models.TextField()
    comments = models.TextField(blank = True)

    VERY_BAD = 1
    BAD = 2
    GOOD = 3
    VERY_GOOD = 4
    EXCELLENT = 5

    RATING_CHOICES = [(VERY_BAD,"Very Bad"),
    (BAD,"Bad"),
    (GOOD,"Good"),
    (VERY_GOOD,"Very Good"),
    (EXCELLENT,"Excellent")]

    rating = models.IntegerField(choices = RATING_CHOICES,default = VERY_BAD)

    def str(self):
        return f'"{self.title}" by {self.author.id}'
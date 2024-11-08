from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=250)
    author_name = models.CharField(max_length=250)
    book_price = models.IntegerField()
    book_quantity = models.IntegerField()
    

    def __str__(self):
        return self.book_name
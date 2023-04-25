from django.db import models

# Create your models here.


class Contact(models.Model):
    fullname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.IntegerField()
    description = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.fullname

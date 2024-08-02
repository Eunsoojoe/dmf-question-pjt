from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    answer_A = models.TextField()
    answer_B = models.TextField()


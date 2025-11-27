from django.db import models

# Create your models here.
class Memo(models.Model):
    text = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)

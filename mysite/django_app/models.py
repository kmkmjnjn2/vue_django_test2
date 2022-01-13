from django.db import models


# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_data = models.DateField()


class LineInfo(models.Model):
    # id = models.IntegerField()
    line = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    value = models.IntegerField()

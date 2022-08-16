from django.db import models

# Create your models here.
class CsvModel(models.Model):
    ISBN = models.BigIntegerField()
    Book_Title = models.CharField(max_length=255,null=True)
    Book_Author = models.CharField(max_length=255,null=True)
    Year_Of_Publication = models.DateField(auto_now=True)
    Publisher = models.CharField(max_length=255,null=True)
    Image_URL_S = models.CharField(max_length=255,null=True)
    Image_URL_M = models.CharField(max_length=255,null=True)
    Image_URL_L = models.CharField(max_length=255,null=True)
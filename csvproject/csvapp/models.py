from django.db import models

# Create your models here.
class CsvModel(models.Model):
    ISBN = models.BigIntegerField()
    Book_Title = models.CharField(max_length=255,null=True)
    Book_Author = models.CharField(max_length=255,null=True)
    Year_Of_Publication = models.BigIntegerField(null=True)
    Publisher = models.CharField(max_length=255,null=True)
    Image_URL_S = models.CharField(max_length=255,null=True)
    Image_URL_M = models.CharField(max_length=255,null=True)
    Image_URL_L = models.CharField(max_length=255,null=True)

    def __str__(self) -> str:
        return self.Book_Title
        
#from csvapp.models import *
#GETED, created = CsvModel.objects.get_or_create(ISBN=12356,Book_Title='JOPA')
import csv

from django.http import HttpResponse
from django.shortcuts import render
from csvapp.models import *
from django.views.generic.base import *


# Create your views here.

class CsvToModel(TemplateView):
    template_name = 'home.html'
    # def post(self, request):
    #     with open('mpathtofile') as f:
    #         reader = csv.reader(f)
    #         for row in reader:
    #             _, created = CsvModel.objects.get_or_create(
    #                 first_name=row[0],
    #                 last_name=row[1],
    #                 middle_name=row[2],
    #                 )
        # return HttpResponse('result')  


    # with open('mpathtofile') as f:
    #         reader = csv.reader(f)
    #         for row in csv_reader:
    #             CsvModel.objects.get_or_create(
    #             ISBN=row[0],
    #             last_name=row[1],
    #             email=row[2],
    #             organisation=row[3],
    #             enrolled=row[4],
    #             last_booking=row[5],
    #             credits_total=row[6],
    #             credits_balance=row[7],
    #             )   
    #         #bulk_create(batch_size=10000)
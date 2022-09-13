import csv

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from csvapp.models import *
from django.views.generic.base import *
from django.views.generic.list import *
from csvapp.forms import UploadForm
import os

class FileUploadView(View):
    form_class = UploadForm
    success_url = reverse_lazy('home')
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('ОТПРАВКА',request.FILES)
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})

class ParseView(View):
    template_name = 'parse.html'

    def get(self, request, *args, **kwargs):
        context = {}
        for filename in os.listdir("media"):
            context[str(filename)] = filename 
        print(context)
        return render(request,'parse.html',{'files':context})

    def post(self, request, *args, **kwargs):
        selected_file = request.POST['selected']
        with open(f'media/{selected_file}') as f:
                reader = csv.reader(f,delimiter=';')
                #counter = 0
                temp_data = []
                for row in reader:
                    temp_data.append(CsvModel(
                    ISBN=row[0] if row[0] != '' else None,
                    Book_Title=row[1] if row[1] != '' else None,
                    Book_Author=row[2] if row[2] != '' else None,
                    Year_Of_Publication=row[3] if row[3] != '' else None,
                    Publisher=row[4] if row[4] != '' else None,
                    Image_URL_S=row[5] if row[5] != '' else None,
                    Image_URL_M=row[6] if row[6] != '' else None,
                    Image_URL_L=row[7] if row[7] != '' else None,
                    ))
                    #counter+=1
                    #print(counter)#принты много потребляют (убирать при работе)
                print('start bulk creation')
                CsvModel.objects.bulk_create(temp_data,batch_size=10000)
                print('finish bulk creation')
        return HttpResponse('Greatly parsed to database')

class DataView(ListView):
    model = CsvModel
    template_name = 'data_list.html'
    paginate_by = 1000 # ?page=3
    
    def get_queryset(self):
        return CsvModel.objects.values('ISBN','Book_Title','Book_Author','Year_Of_Publication','Publisher')


    
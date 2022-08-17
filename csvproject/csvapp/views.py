import csv

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from csvapp.models import *
from django.views.generic.base import *
from django.views.generic.list import *
from csvapp.functions import handle_uploaded_file  
from csvapp.forms import UploadForm


# Create your views here.

#class CsvToModel(TemplateView):
    #template_name = 'home.html'
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

# def index(request):  
#     if request.method == 'POST':  
#         file = UploadForm(request.POST, request.FILES)  #file = form
#         if file.is_valid():  
#             handle_uploaded_file(request.FILES['file'])  
#             return HttpResponse("File uploaded successfuly")  
#     else:  
#         file = UploadForm()  
#         return render(request,"home.html",{'form':file})  

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
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})

def parse(request):
    with open('csvapp/static/upload/books.csv') as f:
            reader = csv.reader(f,delimiter=';')
            counter = 0
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
                counter+=1
                print(counter)
            print('start bulk creation')
            CsvModel.objects.bulk_create(temp_data,batch_size=10000)
            print('finish bulk creation')
    return HttpResponse('Greatly parsed to database')

class DataView(ListView):
    model = CsvModel
    template_name = 'data_list.html'
    paginate_by = 100 # ?page=3
    
    def get_queryset(self):
        return CsvModel.objects.values('ISBN','Book_Title','Book_Author','Year_Of_Publication','Publisher')


    
from dataclasses import fields
from django import forms
from .models import FileUploadModel  

class UploadForm(forms.ModelForm):  
    file = forms.FileField() # for creating file input  
    class Meta:
        model = FileUploadModel
        fields = ['file']

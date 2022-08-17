from django import forms  
class UploadForm(forms.Form):  
    file = forms.FileField() # for creating file input  

# class ParseForm(forms.Form):
#     files = forms.ModelChoiceField()
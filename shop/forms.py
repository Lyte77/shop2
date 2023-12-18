from django import forms
from .models import Product, Category

from django.contrib.auth.models import User

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','image','new_price','old_price','description']
        widgets = {

            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),

            'category':forms.Select(attrs={
                'class':'form-control'
            }),

            
            'image':forms.FileInput(attrs={
                'accept': 'image/*',
                'class':'form-control'
                
            }),

            'new_price':forms.NumberInput(attrs={
                'class':'form-control'
            }),

            'old_price':forms.NumberInput(attrs={
                'class':'form-control'
            }),

            'description':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Optional'
            }),
                

           


        
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['category'].queryset = Category.objects.all()

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False

   

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','image','new_price','description']
        widgets = {
            'image':forms.FileInput(attrs={
                'accept': 'image/*'
            })
        }




class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

    


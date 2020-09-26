from django import forms
from ..models.categories import Category

#Category form
class CategoryForm(forms.ModelForm):
    category_name = forms.CharField( error_messages = { 
                    'required':"Category Name is required"
                 })
                 
    class Meta:
        model = Category
        fields = ('category_name',)
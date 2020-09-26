from django import forms
from ..models.subcategories import Subcategory

#Category form
class SubcategoryForm(forms.ModelForm):
    sub_category_name = forms.CharField( error_messages = { 
                    'required':"Subcategory Name is required"
                 })
    category_id = forms.IntegerField( error_messages = { 
                    'required':"Please select a Category!"
                 })

    class Meta:
        model = Subcategory
        fields = ('sub_category_name', 'category_id')

from django import forms
from .models import *
 
class Enquiryform(forms.ModelForm):
    class Meta:
        model= Enquiry
        fields='__all__'
        
class cartform(forms.ModelForm):
    class Meta:
        model= usercart
        fields='__all__'

class checkoutform(forms.ModelForm):
    class Meta:
        model= checkout
        fields='__all__'


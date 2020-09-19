from django.forms import ModelForm
from . models import Upload
from . models import *


class ApplyForm(ModelForm):


    class Meta:
        model= Upload
        fields='__all__'
        exclude=['user']
# class ImageForm(object):
#     """docstring forImageForm."""
#
#
#
#     class Meta:
#         models = Images2
#         fields='__all__'
#









# class Notefullform(Noteform):
#     images =forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
#     class Meta(Noteform.Meta):
#         fields=Noteform.Meta.fields + ['images',]

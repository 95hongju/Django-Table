from django import forms

class inputForm(forms.Form):
    barcode_num=forms.CharField(max_length=30,label='barcode_num', label_suffix="")
    freeze_num=forms.CharField(max_length=10,label='freeze_num', label_suffix="")
    box_num=forms.CharField(max_length=10, label='box_num', label_suffix="")
    rack_num=forms.CharField(max_length=10, label='rack_num', label_suffix="")
    well_num=forms.CharField(max_length=10, label='well_num', label_suffix="")

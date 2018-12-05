from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic
from .models import tbValues
from django.contrib import messages
import pandas as pd
from io import StringIO


from django import forms

class inputForm(forms.Form):
    barcode_num=forms.CharField(max_length=30,label='barcode_num', label_suffix="")
    freeze_num=forms.CharField(max_length=10,label='freeze_num', label_suffix="")
    box_num=forms.CharField(max_length=10, label='box_num', label_suffix="")
    rack_num=forms.CharField(max_length=10, label='rack_num', label_suffix="")
    well_num=forms.CharField(max_length=10, label='well_num', label_suffix="")



#http://jeremyko.blogspot.com/search/label/Django
# Create your views here.
def index(request):
    tbValues_list=tbValues.objects.all()
    context={'tbValues_list':tbValues_list}
    return render(request,'infos/index.html',context)

def edit(request,id):
    tbvalue=get_object_or_404(tbValues,pk=id)
    tbValues_list=tbValues.objects.all()
    return render(request,'infos/edit.html',{'tbValues_list':tbValues_list,'tbvalue':tbvalue})

def edit_done(request,id):
    original=get_object_or_404(tbValues, pk=id)
    original.barcode_num=request.POST['barcode_num']
    original.freeze_num=request.POST['freeze_num']
    original.box_num=request.POST['box_num']
    original.rack_num=request.POST['rack_num']
    original.well_num=request.POST['well_num']
    original.save()
    return HttpResponseRedirect(reverse('infos:index'))


def remove(request,id):
    tbvalue=tbValues.objects.get(pk=id)
    tbvalue.delete()
    return HttpResponseRedirect(reverse('infos:index'))

def add_new(request):
    form=inputForm(request.POST)
    print(form)
    tb=tbValues(barcode_num=request.POST['barcode_num'],freeze_num=request.POST['freeze_num'],box_num=request.POST['box_num'],rack_num=request.POST['rack_num'],well_num=request.POST['well_num'])
    tb.save()
    return HttpResponseRedirect(reverse('infos:index'))

def search(request):
    option_name=request.POST['option_name']
    search_keyword=request.POST['search']
    tbValues_list=search_result(option_name,search_keyword)
    if search_keyword=='':
        context={'tbValues_list': tbValues_list}
    else:
        result="results '"+search_keyword + "' in "+option_name
        context={'tbValues_list': tbValues_list,'result':result}
    return render(request,'infos/index.html',context)

def search_result(option_name, search_keyword):
    if option_name == 'barcode_num':
        return tbValues.objects.filter(barcode_num__contains=search_keyword)
    elif option_name == 'freeze_num':
        return tbValues.objects.filter(freeze_num__contains=search_keyword)
    elif option_name == 'box_num':
        return tbValues.objects.filter(box_num__contains=search_keyword)
    elif option_name == 'rack_num':
        return tbValues.objects.filter(rack_num__contains=search_keyword)
    elif option_name == 'well_num':
        return tbValues.objects.filter(well_num__contains=search_keyword)

def upload(request):
    if request.FILES.__len__()==0:
        messages.info(request, 'There are no files !')
        return HttpResponseRedirect(reverse('infos:index'))

    uploadfile = request.FILES['file']
    if uploadfile.name.find('txt')<0:
        messages.info(request, ' This is not txt file !')
        return HttpResponseRedirect(reverse('infos:index'))
    read='barcode_num\tfreeze_num\tbox_num\track_num\twell_num\n'
    read+=uploadfile.read().decode('utf8')

    testdata=StringIO(read)
    data=pd.read_csv(testdata,sep='\t')
    print(data)

    #check the null data
    if data.isnull().sum().sum()!=0:
        messages.info(request, 'check the file ! null data in file ')
        return HttpResponseRedirect(reverse('infos:index'))
    else:
        for index,row in data.iterrows():
            tb=tbValues(barcode_num=row['barcode_num'],freeze_num=row['freeze_num'],box_num=row['box_num'],rack_num=row['rack_num'],well_num=row['well_num'])
            tb.save()
        messages.info(request, 'upload done !')
        return HttpResponseRedirect(reverse('infos:index'))

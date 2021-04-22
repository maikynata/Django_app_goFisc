from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import csv, io
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
import logging
from django.urls import reverse
from django import forms
from .models import ModelFormWithFileField
from .models import Tabelaexternareferenciada


def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))

# one parameter named request
def form_upload(request):
    template = "form_upload.html"
    data = Tabelaexternareferenciada.objects.all()

    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address, phone, profile',
        'tabelas': data    
              }

    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']

    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Tabelaexternareferenciada.objects.update_or_create(
            id=column[0],
            tipo=column[1],
            versao=column[2],
            listaufs=column[3],
            hash=column[4]
        )
    context = {}
    return render(request, template, context)











    # if request.method == 'GET':
    #     return render(request, template, prompt)

    #     form = ModelFormWithFileField(request.POST, request.FILES)
    #     if form.is_valid():
    #         # file is saved
    #         form.save()
    #         return HttpResponseRedirect('form_upload.html')
    # else:
    #     form = ModelFormWithFileField()
    # return render(request, 'form_upload.html', {'form': form})
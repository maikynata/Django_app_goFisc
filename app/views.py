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
	
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('form_upload.html')
    else:
        form = ModelFormWithFileField()
    return render(request, 'form_upload.html', {'form': form})
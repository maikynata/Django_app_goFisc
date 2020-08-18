from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import csv, io
from django.contrib import messages
from .models import Reg0200


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
def profile_upload(request):
    # declaring template
    template = "form_upload.html"
    data = Reg0200.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "POST":
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
        _, created = Reg0200.objects.update_or_create(
            name=column[0],
            email=column[1],
            address=column[2],
            phone=column[3],
            profile=column[4]
        )
    context = {}
    return render(request, template, context)


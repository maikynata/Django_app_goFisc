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


# def form_upload(request):
# 	data = {}
# 	if "GET" == request.method:
# 		return render(request, "app/form_upload.html", data)
#     # if not GET, then proceed
# 	try:
# 		csv_file = request.FILES["csv_file"]
# 		if not csv_file.name.endswith('.csv'):
# 			messages.error(request,'File is not CSV type')
# 			return HttpResponseRedirect(reverse("app:form_upload"))
#         #if file is too large, return
# 		if csv_file.multiple_chunks():
# 			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
# 			return HttpResponseRedirect(reverse("app:form_upload"))

# 		file_data = csv_file.read().decode("utf-8")		

# 		lines = file_data.split("\n")
# 		#loop over the lines and save them in db. If error , store as string and then display
# 		for line in lines:						
# 			fields = line.split(",")
# 			data_dict = {}
# 			data_dict["id"] = fields[0]
# 			data_dict["tipo"] = fields[1]
# 			data_dict["versao"] = fields[2]
# 			data_dict["listaufs"] = fields[3]
# 			data_dict["hash"] = fields[4]
# 			try:
# 				form = EventsForm(data_dict)
# 				if form.is_valid():
# 					form.save()					
# 				else:
# 					logging.getLogger("error_logger").error(form.errors.as_json())												
# 			except Exception as e:
# 				logging.getLogger("error_logger").error(repr(e))					
# 				pass

# 	except Exception as e:
# 		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
# 		messages.error(request,"Unable to upload file. "+repr(e))

# 	return HttpResponseRedirect(reverse("app:form_upload"))


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
    csv_file = request.FILES['csv_file']

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
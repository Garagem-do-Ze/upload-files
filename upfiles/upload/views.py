from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import DocumentForm
from .models import Document

def index(request):
    context = {"a":"a"}
    return render(request, "login/index.html", context)

def up(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print (form.cleaned_data['docname'])
            newdoc = Document(
                first_name=form.cleaned_data['first_name'], 
                second_name=form.cleaned_data['second_name'], 
                email=form.cleaned_data['email'], 
                docname=form.cleaned_data['docname'], 
                docfile = request.FILES['docfile'],
                details=form.cleaned_data['details']
            )
            newdoc.save()
            return HttpResponseRedirect('')
        else:
            print (form.cleaned_data['first_name'])
            print (form.cleaned_data['second_name'])
            print (form.cleaned_data['email'])
            print (form.cleaned_data['docname'])
            print (form.cleaned_data['details'])
            
    else:
        form = DocumentForm()
    documents = Document.objects.latest('docfile')
    return render(
        request,
        'success/index.html',
        {'documents': documents, 'form': form}
    )

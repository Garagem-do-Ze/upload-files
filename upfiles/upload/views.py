from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import DocumentForm
from .models import Document
from django.views.decorators.csrf import csrf_protect

def index(request):
    context = {"a":"a"}
    return render(request, "login/index.html", context)

@csrf_protect
def up(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        newdoc = Document(
            first_name = form.data['first_name'], 
            second_name = form.data['second_name'], 
            email = form.data['email'], 
            docname = form.data['docname'], 
            docfile = request.FILES['docfile'],
            details = form.data['details']
        )
        newdoc.save()
        return HttpResponseRedirect('')

    else:
        form = DocumentForm()
    documents = Document.objects.latest('docfile')
    return render(
        request,
        'success/index.html',
        {'documents': documents, 'form': form}
    )

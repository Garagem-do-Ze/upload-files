from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import DocumentForm
from django.template import RequestContext

from .models import Document
from .forms import DocumentForm

def index(request):
    context = {"a":"a"}
    return render(request, "login/index.html", context)

def up(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('upload.views.up'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'success/index.html',
        {'documents': documents, 'form': form}
    )

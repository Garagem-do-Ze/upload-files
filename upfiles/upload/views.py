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
        print('yes is post')
        # form = DocumentForm(request.POST, request.FILES)
        form = DocumentForm(request.POST)

        # print(form)

        if form.is_valid():
            print('first_name')
            # print(form.fields['first_name'])
            print(form.cleaned_data['first_name'])
            # newdoc = Document(docfile = request.FILES['docfile'])
            # newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('')
        else:
            print('noooo, form is invalid!!!')
    else:
        form = DocumentForm() # A empty, unbound form

    documents = Document.objects.latest('docfile')
    # print('documents:')
    # print(documents)
    # print('\nform:')
    # print(form)

    # Render list page with the documents and the form
    return render(
        request,
        'success/index.html',
        {'documents': documents, 'form': form}
    )

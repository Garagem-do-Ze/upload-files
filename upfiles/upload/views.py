from django.shortcuts import render

def index(request):
    context = {"a":"a"}
    return render(request, "login/index.html", context)



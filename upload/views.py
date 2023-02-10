from django.shortcuts import render

def index(request):
    context={

    }
    return render(request, 'uploads/index.html', context)
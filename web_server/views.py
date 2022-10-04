from django.shortcuts import render


def hello_view(request):
    return render(request, 'index.html')

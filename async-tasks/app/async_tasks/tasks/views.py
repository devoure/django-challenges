from django.shortcuts import render, redirect
from . import tasks


# Create your views here.
def index(request):
    context = {"loading": False}

    if request.method == "POST":
        context = {"loading": True}
        tasks.compute.delay()
        return redirect('success')

    return render(request, 'index.html', context)


def success(request):
    return render(request, 'success.html')

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import blouse
from .forms import blouseform
def index(request):
    return render(request, 'indexhtml/blouse.html')


def create(request):
    blouse_form = blouseform(request.POST or None)
    if request.method == 'POST' :
        blouse.objects.create(
             category = request.POST.get('category'),
             size = request.POST.get('size'),
             price = request.POST.get('price'),
        )

        return HttpResponseRedirect('/blouse/')

    context = {
        "title" : 'create',
        'blouse_form' : blouse_form,
    }
    return render(request, 'blouse/create.html', context)
        
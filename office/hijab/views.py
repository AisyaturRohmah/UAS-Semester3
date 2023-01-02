from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import hijab
from .forms import hijabform

def index(request):
    return render(request, 'indexhtml/hijab.html')

def create(request):
    hijab_form = hijabform(request.POST or None)
    if request.method == 'POST' :
        hijab.objects.create(
             warna = request.POST.get('warna'),
             size = request.POST.get('size'),
             price = request.POST.get('price'),
        )

        return HttpResponseRedirect('/produk/')

    context = {
        "title" : 'create',
        'hijab_form' : hijab_form,
    }
    return render(request, 'produk/create.html', context)
        

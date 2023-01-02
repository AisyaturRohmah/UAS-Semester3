from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Toko' 
}
    return render (request, 'Aisyah/index.html', context)
from django.shortcuts import render

from blog.models import Maxsulot, Korinish, Xaridor


# Create your views here.



def index(request):
    maxsulot = Maxsulot.objects.all()
    korinish = Korinish.objects.all()
    xaridor = Xaridor.objects.all()
    context ={
        'maxsulot': maxsulot,
        'korinish': korinish,
        'xaridor': xaridor
    }
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html', context={})

def client(request):
    return render(request, 'client.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})

def products(request):
    maxsulot = Maxsulot.objects.all()

    context ={
        'maxsulot': maxsulot

    }
    return render(request, 'products.html', context=context)


def detail(request, id):
    product = Maxsulot.objects.get(id=id)
    context = {
        'product': product

    }
    return render(request, 'detail.html', context=context)

def clients(request, id):
    customer = Xaridor.objects.get(id=id)
    context = {
        'customer': customer

    }
    return render(request, 'clients.html', context=context)

def banner(request, id):
    banner = Korinish.objects.get(id=id)
    context = {
        'banner': banner
    }
    return render(request, 'banner.html', context=context)
























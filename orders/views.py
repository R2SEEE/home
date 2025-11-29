from django.shortcuts import render



def catalog(request):
    return render(request, 'orders/catalog.html')


def product(request):
    return render(request, 'orders/product.html')
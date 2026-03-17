from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{
        'active_menu':'home'
    })

def supplier(request):
    return render(request,'supplier.html',{
        'active_menu':'supplier'
    })


def stock(request):
    return render(request,'stock.html',{
        'active_menu':'stock'
    })


def sale(request):
    return render(request,'sale.html',{
        'active_menu':'sale'
    })

def savinggold(request):
    return render(request,'savinggold.html',{
        'active_menu':'savinggold'
    })

def report(request):
    return render(request,'report.html',{
        'active_menu':'report'
    })


def setting(request):
    return render(request,'setting.html',{
        'active_menu':'setting'
    })

def search(request):
    return render(request, 'savinggold/search.html', {
        'active_menu': 'search'
    }) 

def saleexport(request):
    return render(request, 'savinggold/saleexport.html', {
        'active_menu': 'saleexport'
    })
from django.shortcuts import render, redirect
from .models import Pods

def pods_list(request):
    podss = Pods.objects.all().order_by('-id')
    return render(request, 'pods_list.html', {'podss': podss})

def pods_detail(request, pk):
    pods = Pods.objects.get(id=pk)
    return render(request, 'pods_detail.html', {'pods': pods})

def create_pods(request):
    if request.method == "POST":
        brand = request.POST['brand']
        desk = request.POST['desk']
        price = request.POST['price']
        image = request.FILES.get('image')

        Pods.objects.create(brand=brand, desk=desk, price=price, image=image)
        return redirect('pods')

    return render(request, 'create_pods.html')

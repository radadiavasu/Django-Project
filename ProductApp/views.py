from django.shortcuts import render

from ProductApp.models import CategoryModel

# Create your views here.
def HomeView(request):
    categoryData = CategoryModel.objects.all()
    print(categoryData)
    return render(request,'home.html',{'categoryKey':categoryData})

def ProductView(request):
    return render(request,'product.html')
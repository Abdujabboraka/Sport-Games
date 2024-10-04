from django.shortcuts import render, redirect
from .models import Category, Sport
# Create your views here.

def homepage(request):
    categories = Category.objects.all()
    sports = Sport.objects.all()
    context = {'categories': categories, 'sports': sports}
    return render(request, 'homepage.html', context)




def select_by_category(request, category_id):
    sports = Sport.objects.filter(category=category_id)
    categories = Category.objects.all()
    context = {'categories': categories, 'sports': sports}
    return render(request, 'homepage.html', context)

def add_sport(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        category_id = request.POST['category']
        image = request.FILES['image']
        category = Category.objects.get(id=category_id)
        sport = Sport(name=name, description=description, image=image, category=category)
        sport.save()
        return redirect('homepage')
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'add_sport.html', context)

def add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = Category(name=name)
        category.save()
        return redirect('homepage')
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'add_category.html', context)









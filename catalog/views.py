from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Каталог алкогольной продукции',
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Пользователь: {name}, контактный телефон: {phone}, сообщение: {message}")

    context = {
        'title': 'Контакты',
    }

    return render(request, 'catalog/contacts.html', context)

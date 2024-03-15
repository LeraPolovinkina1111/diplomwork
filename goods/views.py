from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render

from goods.models import Products


def catalog(request):
    contex: dict[str, any] = {
        'title': 'Home - Каталог',
        'goods': [
            {'image': 'deps/images/goods/bread.jpg',
             'name': 'Хлеб',
             'description': 'Обычный хлеб',
             'price': 30.00},

            {'image': 'deps/images/goods/bread1.jpg',
             'name': 'Хлеб',
             'description': 'Ржаной хлеб',
             'price': 30.00},
            {'image': 'deps/images/goods/bread2.jpg',
             'name': 'Хлеб',
             'description': 'Ржаной хлеб',
             'price': 30.00},

            {'image': 'deps/images/goods/milk2.jpg',
             'name': 'Молоко',
             'description': 'Молоко Деревенское',
             'price': 93.00},

            {'image': 'deps/images/goods/smetana.jpg',
             'name': 'Сметана',
             'description': 'Сметана Шадринская',
             'price': 67.00},

            {'image': 'deps/images/goods/muka.jpg',
             'name': 'Мука',
             'description': 'Мука твердого помола',
             'price': 30.00},

        ]
    }

    return render(request, "goods/catalog.html", contex)


def milk(request):
    contex: dict[str, any] = {
        'title': 'Home - Каталог',
        'goods': [

            {'image': 'deps/images/goods/milk2.jpg',
             'name': 'Молоко',
             'description': 'Молоко Деревенское',
             'price': 93.00},

            {'image': 'deps/images/goods/smetana.jpg',
             'name': 'Сметана',
             'description': 'Сметана Шадринская',
             'price': 67.00},

        ]
    }

    return render(request, "goods/catalog.html", contex)


def bread(request):
    contex: dict[str, any] = {
        'title': 'Home - Каталог',
        'goods': [
            {'image': 'deps/images/goods/bread.jpg',
             'name': 'Хлеб',
             'description': 'Обычный хлеб',
             'price': 30.00},

            {'image': 'deps/images/goods/bread1.jpg',
             'name': 'Хлеб',
             'description': 'Ржаной хлеб',
             'price': 30.00},
            {'image': 'deps/images/goods/bread2.jpg',
             'name': 'Хлеб',
             'description': 'Ржаной хлеб',
             'price': 30.00},

        ]
    }

    return render(request, "goods/catalog.html", contex)


def bacaleya(request):
    contex: dict[str, any] = {
        'title': 'Home - Каталог',
        'goods': [
            {'image': 'deps/images/goods/muka.jpg',
             'name': 'Мука',
             'description': 'Мука твердого помола',
             'price': 30.00},
            ]

    }

    return render(request, "goods/catalog.html", contex)


def product(request, product_slug):
    product: object = Products.objects.get(slug=product_slug)

    context = {"product": product}

    return render(request, "goods/product.html", context=context)

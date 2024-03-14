from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render


def catalog(request):
    contex: dict[str, any] = {
        'title': 'Home - Каталог',
        'goods': [
            {'image': 'deps/images/goods/bread.jpg',
             'name': 'Хлеб',
             'description': 'Обычный хлеб',
             'price': 30.00},

            {'image': 'deps/images/goods/milk1.jpg',
             'name': 'Молоко',
             'description': 'Молоко Талицкое',
             'price': 93.00},

            {'image': 'deps/images/goods/smetana.jpg',
             'name': 'Сметана',
             'description': 'Сметана Шадринская',
             'price': 67.00},

            {'image': 'deps/images/goods/kitchen table.jpg',
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

            {'image': 'deps/images/goods/milk1.jpg',
             'name': 'Молоко',
             'description': 'Молоко Талицкое',
             'price': 93.00},

            {'image': 'deps/images/goods/smetana.jpg',
             'name': 'Сметана',
             'description': 'Сметана Шадринская',
             'price': 67.00},

        ]
    }

    return render(request, "goods/catalog.html", contex)


def product(request, product_slug):
    return render(request, "goods/product.html")

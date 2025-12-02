from django.shortcuts import render

carts = [
        {'image': 'images/photo_carts/sofa.jpg',
         'name': 'Набор чайной мебели с тремя стульями',
         'description': 'Элегантный комплект для уютных посиделок: компактный столик и три стильных стула.',
         'price': 158.00},

        {'image': 'images/photo_carts/set of tea table and three chairs.jpg',
         'name': 'Мини-набор для чайной зоны',
         'description': 'Столик и два аккуратных стула — идеальное решение для кухни или маленькой гостиной.',
         'price': 97.00},

        {'image': 'images/photo_carts/office chair.jpg',
         'name': 'Кровать двуспальная с мягким изголовьем',
         'description': 'Комфортная кровать с ортопедическим основанием и мягкой отделкой изголовья.',
         'price': 690.00},

        {'image': 'images/photo_carts/sofa.jpg',
         'name': 'Кухонный стол с встроенной мойкой',
         'description': 'Практичный кухонный модуль с рабочей поверхностью, раковиной и удобным местом для обедов.',
         'price': 372.00},

        {'image': 'images/photo_carts/office chair.jpg',
         'name': 'Многофункциональный кухонный остров',
         'description': 'Удобный стол с варочной поверхностью, раковиной и большим количеством отделений для хранения.',
         'price': 445.00},

        {'image': 'images/photo_carts/office chair.jpg',
         'name': 'Просторный угловой диван',
         'description': 'Комфортный раскладной диван, который легко превращается в большую двуспальную кровать.',
         'price': 625.00},
    ]

def catalog(request):

    context = {
        'title': 'catalog',
        'carts': carts,

    }
    return render(request, 'orders/catalog.html', context)


def product(request):
    return render(request, 'orders/product.html')

from django.db import models



class Categories(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name='Категория')
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True, verbose_name='URL')

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "Категории"
        db_table = 'category'



class Products(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name='Категория')
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True, verbose_name='URL')
    text = models.TextField(blank=True, null=True, verbose_name='Описание товара')
    image = models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='Изображения')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, verbose_name='Цена')
    discount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, verbose_name='Скидка %')
    stock = models.PositiveIntegerField(default=0, verbose_name='Остаток товара') # количество
    category_id = models.ForeignKey(to=Categories, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "продук"
        verbose_name_plural = "Продукты"
        db_table = 'products'

from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=500, verbose_name='Имя')

    class Meta:
        verbose_name = 'Категорий продукты'
        verbose_name_plural = 'Категорий продукты'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=500, verbose_name='Имя')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'продукты'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.title

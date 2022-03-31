from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    pack = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/products')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)



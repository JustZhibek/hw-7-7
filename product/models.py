from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    @property
    def category_name(self):
        try:
            return self.category.name
        except:
            return 'No categories'

    @property
    def rating(self):
        stars_list = [review.stars for review in self.reviews.all()]
        return round(sum(stars_list) / len(stars_list), 2)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=120)
    @property
    def products_count(self):
        return self.product_set.count()

    def product_list(self):
        return [product.title for product in self.product_set.all()]

    def __str__(self):
        return self.name

class Review(models.Model):
    CHOICES = ((i, "*" * i) for i in range(1, 6))
    text = models.TextField(blank=True, null=True)
    product = models.ForeignKey('Category', on_delete=models.CASCADE)
    stars = models.IntegerField(choices=CHOICES, default=0)


    def __str__(self):
        return self.text

    @property
    def product_title(self):
        return self.product.title
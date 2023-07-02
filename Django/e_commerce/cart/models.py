from django.db import models
from base.models import User
from products.models import ProductItem

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(ProductItem, through='CartItem')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


class CartItem(models.Model):
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
    @property
    def total_price(self):
        return self.product.price * self.quantity 
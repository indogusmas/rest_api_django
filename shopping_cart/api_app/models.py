from django.db import models

# Create your models here.

class CartItem(models.Model):
    product_name = models.CharField(max_length=250)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()


    # class Meta:
    #     verbose_name = _("CartItem")
    #     verbose_name_plural = _("CartItems")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("CartItem_detail", kwargs={"pk": self.pk})


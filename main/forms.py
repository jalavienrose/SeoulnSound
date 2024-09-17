from django.forms import ModelForm
from main.models import Shop

class ShopEntryForm(ModelForm):
    class Meta:
        model = Shop
        fields = ["product_name", "price", "description", "rating"]
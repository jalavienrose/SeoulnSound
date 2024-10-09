from django.forms import ModelForm
from main.models import Shop
from django.utils.html import strip_tags

class ShopEntryForm(ModelForm):
    class Meta:
        model = Shop
        fields = ["product_name", "price", "description", "rating"]

    def clean_product_name(self):
        product_name = self.cleaned_data["product_name"]
        return strip_tags(product_name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
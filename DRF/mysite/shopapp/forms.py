from django import forms

from shopapp.models import Product


class MultipleFileInput(forms.FileInput):
    allow_multiple_selected = True


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount", "preview"

    #images = forms.ImageField(
    #    widget=forms.ClearableFileInput(attrs={"multiple": True}),
    #)
    images = forms.ImageField(
        widget=MultipleFileInput(attrs={"multiple": True}),
        required=False,
    )

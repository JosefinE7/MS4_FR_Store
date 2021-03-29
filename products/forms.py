from django import forms
from .models import Product, Category, RatingProducts, RATE_SCALE


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            categories = Category.objects.all()
            friendly_names = [(c.id, c.get_friendly_name())
                              for c in categories]

            self.fields['category'].choices.friendly_names
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-black rounded-0'


class RatingProductsForm(forms.ModelForm):

    class Meta:
        model = RatingProducts
        fields = ('rate_comment', 'rate')

    rate_comment = forms.CharField(
        widget=forms.Textarea(), max_length=2500, required=False
    )
    rate = forms.ChoiceField(
        choices=RATE_SCALE, widget=forms.Select(), required=True)

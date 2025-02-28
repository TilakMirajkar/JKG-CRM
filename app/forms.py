from django import forms
from .models import ItemInformation, ItemAttributes, ItemClassification, ItemLocation, ItemTax, ItemReorder, ItemManufacturing

class ItemInformationForm(forms.ModelForm):
    class Meta:
        model = ItemInformation
        fields = '__all__'

class ItemAttributesForm(forms.ModelForm):
    class Meta:
        model = ItemAttributes
        fields = '__all__'

class ItemClassificationForm(forms.ModelForm):
    class Meta:
        model = ItemClassification
        fields = '__all__'

class ItemLocationForm(forms.ModelForm):
    class Meta:
        model = ItemLocation
        fields = '__all__'

class ItemTaxForm(forms.ModelForm):
    class Meta:
        model = ItemTax
        fields = '__all__'

class ItemReorderForm(forms.ModelForm):
    class Meta:
        model = ItemReorder
        fields = '__all__'

class ItemManufacturingForm(forms.ModelForm):
    class Meta:
        model = ItemManufacturing
        fields = '__all__'
from django.db import models

class ItemInformation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    sku = models.CharField(max_length=100, unique=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_order_quantity = models.IntegerField()
    supplier = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ItemAttributes(models.Model):
    item = models.OneToOneField(ItemInformation, on_delete=models.CASCADE, related_name='attributes')
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    discount_levels = models.JSONField()
    country_of_origin = models.CharField(max_length=100)
    images = models.ImageField(upload_to='item_images/')
    category = models.CharField(max_length=100)
    packaging_info = models.TextField()
    margin = models.DecimalField(max_digits=5, decimal_places=2)
    production_cost = models.DecimalField(max_digits=10, decimal_places=2)
    variations = models.JSONField()

class ItemClassification(models.Model):
    item = models.OneToOneField(ItemInformation, on_delete=models.CASCADE, related_name='classification')
    classification_code = models.CharField(max_length=100)
    default_unit_of_measure = models.CharField(max_length=50)
    unit_of_measure_conversions = models.JSONField()

class ItemLocation(models.Model):
    item = models.OneToOneField(ItemInformation, on_delete=models.CASCADE, related_name='location')
    branch_plant = models.CharField(max_length=255)
    primary_location = models.CharField(max_length=255)
    secondary_location = models.CharField(max_length=255)

class ItemTax(models.Model):
    item = models.OneToOneField(ItemInformation, on_delete=models.CASCADE, related_name='tax')
    tax_info = models.JSONField()

class ItemReorder(models.Model):
    item = models.OneToOneField(ItemInformation, on_delete=models.CASCADE, related_name='reorder')
    reorder_quantity = models.IntegerField()

class ItemManufacturing(models.Model):
    item = models.OneToOneField(ItemInformation, on_delete=models.CASCADE, related_name='manufacturing')
    branch_plant = models.CharField(max_length=255)
    manufacturing_info = models.TextField()
from django.shortcuts import render, get_object_or_404, redirect
from .models import ItemInformation, ItemAttributes, ItemClassification, ItemLocation, ItemTax, ItemReorder, ItemManufacturing
from django.db.models import Sum
from .forms import ItemInformationForm, ItemAttributesForm, ItemClassificationForm, ItemLocationForm, ItemTaxForm, ItemReorderForm, ItemManufacturingForm

def item_list(request):
    items = ItemInformation.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(ItemInformation, pk=pk)
    return render(request, 'item_detail.html', {'item': item})

def item_create(request):
    if request.method == 'POST':
        form = ItemInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemInformationForm()
    return render(request, 'item_form.html', {'form': form})

def item_update(request, pk):
    item = get_object_or_404(ItemInformation, pk=pk)
    if request.method == 'POST':
        form = ItemInformationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemInformationForm(instance=item)
    return render(request, 'item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(ItemInformation, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_delete.html', {'item': item})

def item_attributes_create(request, item_id):
    item = get_object_or_404(ItemInformation, id=item_id)
    if request.method == 'POST':
        form = ItemAttributesForm(request.POST, request.FILES)
        if form.is_valid():
            attributes = form.save(commit=False)
            attributes.item = item
            attributes.save()
            return redirect('item_detail', pk=item_id)
    else:
        form = ItemAttributesForm()
    return render(request, 'item_attributes_form.html', {'form': form, 'item': item})

def item_classification_create(request, item_id):
    item = get_object_or_404(ItemInformation, id=item_id)
    if request.method == 'POST':
        form = ItemClassificationForm(request.POST)
        if form.is_valid():
            classification = form.save(commit=False)
            classification.item = item
            classification.save()
            return redirect('item_detail', pk=item_id)
    else:
        form = ItemClassificationForm()
    return render(request, 'item_classification_form.html', {'form': form, 'item': item})

def item_location_create(request, item_id):
    item = get_object_or_404(ItemInformation, id=item_id)
    if request.method == 'POST':
        form = ItemLocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.item = item
            location.save()
            return redirect('item_detail', pk=item_id)
    else:
        form = ItemLocationForm()
    return render(request, 'item_location_form.html', {'form': form, 'item': item})

def item_tax_create(request, item_id):
    item = get_object_or_404(ItemInformation, id=item_id)
    if request.method == 'POST':
        form = ItemTaxForm(request.POST)
        if form.is_valid():
            tax = form.save(commit=False)
            tax.item = item
            tax.save()
            return redirect('item_detail', pk=item_id)
    else:
        form = ItemTaxForm()
    return render(request, 'item_tax_form.html', {'form': form, 'item': item})

def item_reorder_create(request, item_id):
    item = get_object_or_404(ItemInformation, id=item_id)
    if request.method == 'POST':
        form = ItemReorderForm(request.POST)
        if form.is_valid():
            reorder = form.save(commit=False)
            reorder.item = item
            reorder.save()
            return redirect('item_detail', pk=item_id)
    else:
        form = ItemReorderForm()
    return render(request, 'item_reorder_form.html', {'form': form, 'item': item})

def item_manufacturing_create(request, item_id):
    item = get_object_or_404(ItemInformation, id=item_id)
    if request.method == 'POST':
        form = ItemManufacturingForm(request.POST)
        if form.is_valid():
            manufacturing = form.save(commit=False)
            manufacturing.item = item
            manufacturing.save()
            return redirect('item_detail', pk=item_id)
    else:
        form = ItemManufacturingForm()
    return render(request, 'item_manufacturing_form.html', {'form': form, 'item': item})

def inventory_report(request):
    total_items = ItemInformation.objects.count()
    total_quantity = ItemInformation.objects.aggregate(Sum('quantity_in_stock'))['quantity_in_stock__sum']
    return render(request, 'reports.html', {
        'total_items': total_items,
        'total_quantity': total_quantity,
    })
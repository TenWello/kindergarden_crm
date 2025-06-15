from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from .models import Inventory
from .forms import InventoryForm
from ingredient.models import Ingredient



def import_products_to_inventory(request):
    if request.method == 'POST':
        product_ids = request.POST.getlist('products')
        for pid in product_ids:
            product = Product.objects.get(id=pid)
            # Agar product allaqachon inventoryda bo'lsa, o'tkazib yuboramiz
            if not Inventory.objects.filter(product=product).exists():
                Inventory.objects.create(
                    name=product.name,
                    product=product
                )
        return redirect('inventory_list')
    products = Product.objects.all()
    return render(request, 'inventory/import_products.html', {'products': products})
def inventory_list(request):
    products = Product.objects.all()  # Barcha productlarni olamiz
    inventories = Inventory.objects.all()
    return render(request, 'inventory/inventory_list.html', {
        'products': products,
        'inventories': inventories,
    })

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/ingredient_list.html', {'ingredients': ingredients})
def inventory_add_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            inv = form.save(commit=False)
            inv.product = product
            inv.name = product.name  # avtomatik nomini oladi
            inv.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(initial={'product': product})
    return render(request, 'inventory/inventory_form.html', {'form': form, 'product': product})
def inventory_edit(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'inventory/inventory_form.html', {'form': form, 'title': "Inventarni tahrirlash"})

def inventory_delete(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        inventory.delete()
        return redirect('inventory_list')
    return render(request, 'inventory/inventory_confirm_delete.html', {'inventory': inventory})

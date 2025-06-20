from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    add_form = ProductForm()
    edit_forms = {p.id: ProductForm(instance=p) for p in products}
    context = {
        'products': products,
        'add_form': add_form,
        'edit_forms': edit_forms,
    }
    return render(request, 'product_list.html', context)

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('product_list')

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
    return redirect('product_list')

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
    return redirect('product_list')

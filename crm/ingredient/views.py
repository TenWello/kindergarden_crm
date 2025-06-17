from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingredient
from .forms import IngredientForm

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredient/ingredient_list.html', {'ingredients': ingredients})

def ingredient_add(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'ingredient/ingredient_form.html', {'form': form, 'title': 'Yangi ingredient qo‘shish'})

def ingredient_edit(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'ingredient/ingredient_form.html', {'form': form, 'title': 'Ingredientni tahrirlash'})

def ingredient_delete(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient_list')
    return render(request, 'ingredient/ingredient_confirm_delete.html', {'ingredient': ingredient})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingredient
from .forms import IngredientForm
from django.contrib.auth.decorators import login_required
from functools import wraps

def role_required(roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if request.user.role not in roles:
                return redirect('forbidden')  # Forbidden page yozamiz
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

@login_required
@role_required([1, 3])  # 1-Admin, 3-Menejer
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredient/list.html', {'ingredients': ingredients})

@login_required
@role_required([1, 3])
def ingredient_create(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'ingredient/form.html', {'form': form})

@login_required
@role_required([1, 3])
def ingredient_update(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'ingredient/form.html', {'form': form})

@login_required
@role_required([1, 3])
def ingredient_delete(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient_list')
    return render(request, 'ingredient/confirm_delete.html', {'ingredient': ingredient})

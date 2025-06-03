from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingredient
from .forms import IngredientForm
from django.contrib.auth.decorators import login_required

@login_required
def ingredient_manage(request):
    ingredients = Ingredient.objects.all()
    add_form = IngredientForm(request.POST or None, prefix='add')
    if request.method == 'POST' and 'add' in request.POST:
        if add_form.is_valid():
            add_form.save()
            return redirect('ingredient_manage')

    edit_forms = {}
    for ing in ingredients:
        if request.method == 'POST' and f'edit-{ing.id}' in request.POST:
            form = IngredientForm(request.POST, instance=ing, prefix=f'edit-{ing.id}')
            if form.is_valid():
                form.save()
                return redirect('ingredient_manage')
            edit_forms[ing.id] = form
        else:
            edit_forms[ing.id] = IngredientForm(instance=ing, prefix=f'edit-{ing.id}')

    context = {
        'ingredients': ingredients,
        'add_form': add_form,
        'edit_forms': edit_forms,
    }
    return render(request, 'ingredients.html', context)

@login_required
def ingredient_delete(request, pk):
    ing = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ing.delete()
    return redirect('ingredient_manage')

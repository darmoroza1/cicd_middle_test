from django.shortcuts import render
from .models import Recipe, Category


def main(request):
    latest_recipes = Recipe.objects.order_by('-created_at')[:5]
    context = {'latest_recipes': latest_recipes}
    return render(request, 'main.html', context)


def category_list(request):
    categories = Category.objects.all()
    category_data = []

    for category in categories:
        recipe_count = Recipe.objects.filter(category=category).count()
        category_data.append({'category': category, 'recipe_count': recipe_count})

    context = {'category_data': category_data}
    return render(request, 'category_list.html', context)



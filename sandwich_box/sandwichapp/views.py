from django.shortcuts import render

from django.views import View
from django.http import Http404
import random

# Ingredients data dictionary
ingredients = {
    'meats': ['ham', 'bacon', 'turkey', 'chicken', 'meatball', 'chorizo'],
    'cheeses': ['cheddar', 'provolone', 'muenster', 'american', 'feta', 'mozzarella'],
    'toppings': ['lettuce', 'tomato', 'pickles', 'onions', 'peppers', 'ranch dressing']
}

# Create your views here.
class SandwichappView(View):
    def get(self, request):
        # pass the keys to the ingredients dictionary to the template
        context = {'ingredients': ingredients.keys()}
        return render(request, 'sandwichapp.html', context=context)

class IngredientsView(View):
    def get(self, request, ingredient_type):
        if request.method == 'GET':
            if ingredient_type not in ingredients:
                raise Http404(f'No such ingredient: {ingredient_type}')

            return render(
                request = request,
                template_name = 'ingredientslist.html',
                context={ 'ingredients': ingredients[ingredient_type],
                            'ingredient_type': ingredient_type }
            )

class SandwichGeneratorView(View):
    def get(self, request):
        # Generate a random sandwich from the ingredients dictionary
        random_meat = random.choice(ingredients['meats'])
        random_cheese = random.choice(ingredients['cheeses'])
        random_topping = random.choice(ingredients['toppings'])
        # Format the sandwich string
        random_sandwich = f'{random_meat} sandwich with {random_cheese} cheese and {random_topping}'
        
        return render(
            request=request, 
            template_name='sandwichgenerator.html', 
            context={'random_sandwich': random_sandwich}
        )
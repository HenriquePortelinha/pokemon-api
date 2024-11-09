# pokemon_app/views.py
from django.shortcuts import render
from .models import Pokemon

def pokemon_list(request):

    pokemons = Pokemon.objects.all()

    return render(request, 'pokemon_list.html', {'pokemons': pokemons})

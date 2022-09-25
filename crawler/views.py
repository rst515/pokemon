'''
Views for the Pokemon database.
'''

from django.views.generic import ListView, DetailView
from .models import Pokemon

API_URL = "http://pokeapi.co/api/v2/pokemon"


class PokemonListView(ListView):
    '''List view of all Pokemon in the database.'''
    model = Pokemon
    paginate_by = 8


class UpdatePokemon(PokemonListView):
    '''Update Pokemon from API and show the list view.'''
    def get_context_data(self, **kwargs):
        added_items = Pokemon.update(self)
        context = super().get_context_data(**kwargs)
        if added_items > 0:
            context['messages'] = f"{added_items} new Pokemon added!"
        else:
            context['messages'] = "No new Pokemon to add right now."

        return context


class PokemonDetailView(DetailView):
    '''Detailed view of a single Pokemon in the database.'''
    queryset = Pokemon.objects.all()

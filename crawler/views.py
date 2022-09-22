'''
Views for the Pokemon database.
'''

from django.views.generic import ListView, DetailView
from .models import Pokemon


class PokemonListView(ListView):
    '''List view of all Pokemon in the database.'''
    model = Pokemon
    paginate_by = 8


class PokemonDetailView(DetailView):
    '''Detailed view of a single Pokemon in the database.'''
    queryset = Pokemon.objects.all()

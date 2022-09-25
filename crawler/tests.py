'''
Unit tests for crawler app.
'''

from django.test import TestCase
from .models import Pokemon
import requests

API_URL = "http://pokeapi.co/api/v2/pokemon"


class AppTests(TestCase):

    def test_connection_to_api(self):
        '''Test the API is available and responding by checking a call returns
        a non-empty list and save the result to the database.'''
        response = requests.get(API_URL)

        self.assertTrue(response.status_code, 200)

    def test_saving_API_records_to_database(self):
        '''Test getting API records and saving to the database.'''
        response = requests.get(API_URL)
        count = response.json()['count']

        all_pokemon_url = API_URL + f"?limit={count}"
        poke_list = requests.get(all_pokemon_url)
        results = poke_list.json()['results']

        for i in range(1, count):
            pokemon = requests.get(results[i]['url']).json()
            sprite = pokemon['sprites']['other']['official-artwork']['front_default']

            new_record = Pokemon(
                pokemon_id=pokemon['id'],
                name=pokemon['name'],
                height=pokemon['height'],
                abilities=[
                    ability['ability']['name'] for ability in pokemon['abilities']
                    ],
                moves=len(pokemon['moves']),
                official_artwork=sprite,
            )
            new_record.save()

        self.assertEqual(Pokemon.objects.all().count(), count-1)

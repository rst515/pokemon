'''
Unit tests for crawler app.
'''

from django.test import TestCase
from .models import Pokemon

import pokebase as pb


class AppTests(TestCase):

    def test_connection_to_api(self):
        '''Test the API is available and responding by checking a call returns
        a non-empty list and save the result to the database.'''
        poke_list = pb.APIResource('pokemon', '')

        self.assertTrue(poke_list.count >= 1)

    def test_saving_API_records_to_database(self):
        '''Test getting API records and saving to the database.'''
        count = 5  # Limit to the first 5 entries otherwise will be
        # waiting all day!

        for i in range(1, count):
            pokemon = pb.APIResource('pokemon', i)
            sprite = pb.SpriteResource(
                'pokemon', i,
                other=True,
                official_artwork=True
                )

            new_record = Pokemon(
                pokemon_id=pokemon.id,
                name=pokemon.name,
                height=pokemon.height,
                abilities=[
                    ability.ability.name for ability in pokemon.abilities
                    ],
                moves=len(pokemon.moves),
                official_artwork=sprite.url,
            )
            new_record.save()

        self.assertEqual(Pokemon.objects.all().count(), count-1)

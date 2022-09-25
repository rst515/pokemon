'''
Database models.
'''

from django.db import models
import requests

API_URL = "http://pokeapi.co/api/v2/pokemon"


class Pokemon(models.Model):
    '''Model to store individual pokemon records.'''
    pokemon_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    height = models.IntegerField()
    abilities = models.CharField(max_length=200)
    moves = models.IntegerField()
    official_artwork = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.pokemon_id} {self.name}"

    def update(self):
        '''Update database from the Pokemon API by adding new records.'''
        db_count = Pokemon.objects.all().count()
        response = requests.get(API_URL)
        api_count = response.json()['count']
        difference = api_count - db_count

        if difference:
            print(f"{difference} new Pokemon found! Adding to database...")
            all_pokemon_url = API_URL + f"?limit={api_count}"
            poke_list = requests.get(all_pokemon_url)
            results = poke_list.json()['results']

            for i in range(db_count, api_count):
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
                print(f"Saving {i}: {new_record.pokemon_id} {new_record.name}")

            print(f"Task complete! Saved {difference} new items.")
        else:
            print(f"Database has {db_count} items and is up-to-date, no new items.")
        return difference

    class Meta():
        ordering = ['pokemon_id']

'''
Script to populate database from API.
'''

from crawler.models import Pokemon

import pokebase as pb


def run():
    '''Clear and repopulate entire database from the Pokemon API.'''
    if Pokemon.objects.all().count() >= 1:
        Pokemon.objects.all().delete()

    # poke_list = pb.APIResource('pokemon', '')
    # count = poke_list.count

    # return the first 100 only, uncomment count above and comment-out 2 lines below to change
    print('''Only the first 100 will be saved, to change this edit
    scripts/refresh.py''')
    count = 100

    for i in range(1, count):
        pokemon = pb.APIResource('pokemon', i)
        print("Processing", pokemon.name)
        sprite = pb.SpriteResource(
            'pokemon', i,
            other=True,
            official_artwork=True
            )

        new_record = Pokemon(
            pokemon_id=pokemon.id,
            name=pokemon.name,
            height=pokemon.height,
            abilities=[ability.ability.name for ability in pokemon.abilities],
            moves=len(pokemon.moves),
            official_artwork=sprite.url,
        )
        new_record.save()
        print(Pokemon.objects.all().count())

    print("Task complete!")

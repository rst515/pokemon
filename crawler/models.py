'''
Database models.
'''

from django.db import models


class Pokemon(models.Model):
    '''Model to store individual pokemon records.'''
    pokemon_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    height = models.IntegerField()
    abilities = models.CharField(max_length=200)
    moves = models.IntegerField()
    official_artwork = models.CharField(max_length=200, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pokemon_id} {self.name}"

    def admin_image(self):
        return '<img src="%s"/>' % self.official_artwork
    admin_image.allow_tags = True

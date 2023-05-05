from django.db import models

class Recette(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    temps_preparation = models.PositiveIntegerField()
    temps_cuisson = models.PositiveIntegerField()
    personnes = models.PositiveIntegerField()

    def __str__(self):
        return self.nom
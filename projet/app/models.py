from django.db import models

class Ingredient(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

# Modèle pour les plats
class Plat(models.Model):
    nom = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient)
    image = models.ImageField(upload_to='plats/')
    hot = models.BooleanField(default=False)
    vegetarien = models.BooleanField(default=False)
    
    # Choix pour le type de plat
    TYPE_PLAT_CHOICES = (
        ('entree', 'Entrée'),
        ('plat_principal', 'Plat Principal'),
        ('dessert', 'Dessert'),
        ('boisson', 'Boisson'),
    )
    type_plat = models.CharField(max_length=20, choices=TYPE_PLAT_CHOICES)

    def __str__(self):
        return self.nom
    
class LoadingPage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='plats/')
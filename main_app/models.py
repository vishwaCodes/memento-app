from django.db import models

# Create your models here.

class Photobook:
    def __init__(self, name, theme, description):
        self.name = name
        self.theme = theme
        self.description = description
        
photobooks = [
    Photobook('Art', 'Color Block', 'A collection of all the Art I made in 2019'),
    Photobook('Best Friend and I', 'Minimal Black', 'All the crazy fun memories with my best friend so far'),
    Photobook('Lavender', 'Minimal White', 'Photos captured based off of everything Lavender')
]       

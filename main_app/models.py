from django.db import models

# Create your models here.

class Photobook(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    
    def __str__(self):
        return self.name 
    

class Photo(models.Model):
    photobook = models.ForeignKey(Photobook, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    
    def __str__(self):
        return self.description 






# class Photobook:
#     def __init__(self, name, theme, description):
#         self.name = name
#         self.theme = theme
#         self.description = description
        
# photobooks = [
#     Photobook('Art', 'Color Block', 'A collection of all the Art I made in 2019'),
#     Photobook('Celadon', 'Minimal Black', 'Photos captured based off of the color Celadon'),
#     Photobook('Lavender', 'Minimal White', 'Photos captured based off of everything Lavender')
# ]       

# art = Photobook('Art', 'Color Block', 'A collection of all the Art I made in 2019')
# celadon = Photobook('Celadon', 'Minimal Black', 'Photos captured based off of the color Celadon')
# lavender = Photobook('Lavender', 'Minimal White', 'Photos captured based off of everything Lavender')

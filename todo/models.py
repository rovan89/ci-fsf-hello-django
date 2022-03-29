from django.db import models

# Create your models here.

 
class Item(models.Model):
    name = models.Charfield(max_lenght=50, null=False, blank=False)
    done = models.Booleanfield(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
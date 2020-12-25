from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Thread (models.Model):
    
    STYLES = (
        ('Embroidery Floss', 'Embroidery Floss'),
        ('Craft Cord', 'Craft Cord'),
        ('Waxed Cord', 'Waxed Cord'),
    )

    brand = models.CharField(max_length=200)
    style = models.CharField(max_length=200, choices=STYLES)
    #TODO make this validate numbers above 0
    id_number = models.IntegerField()
    color_name = models.CharField(max_length=250)
    length_owned = models.DecimalField(max_digits=50, decimal_places=2)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('brand',)

    def __str__(self):
        return ('{0} {1} #{2}: {3}. {4} meters owned.'.format(self.brand, self.style, self.id_number, self.color_name, self.length_owned))    
 

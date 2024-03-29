from django.db import models

# Create your models here.
class Stock(models.Model):


    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    choices = (

        ('AVIALABLE','Item ready to be purchase'),
        ('SOLD','Item already sold out'),
        ('RESTOcKING','Item will be restocking in few days')

    )
    status = models.CharField(max_length=10,choices=choices ,default="SOLD")
    issues = models.CharField(max_length=100,default="NO ISSUES")

    class Meta:
        abstract = True

    def __str__(self):

        return 'Type : {0} Price : {1}'.format(self.type,self.price)

class Nighty(Stock):
    pass

class Inskirt(Stock):
    pass

class Blouse(Stock):
    pass

class Saree(Stock):
    pass



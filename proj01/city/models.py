from django.db import models

class City(models.Model):
    key = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=20)
    population = models.IntegerField(default=0)
    date_mod = models.DateField()

    def __str__(self):
        return '<Friend:id=' + str(self.id) + ', ' + \
            self.key + ', ' + self.name + '>'

from django.db import models

# Create your models here.
class Problem(models.Model):
    name = models.CharField(max_length=500)
    prob_id = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    tags = models.CharField(max_length = 500)
    

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
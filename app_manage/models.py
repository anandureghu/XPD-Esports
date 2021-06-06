from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=20, blank=False, default="")

    def __str__(self):
        return self.title


class Managing(models.Model):
    position = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return self.position 


class Role(models.Model):
    title = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Lineup(models.Model):
    title = models.CharField(max_length=30)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.title
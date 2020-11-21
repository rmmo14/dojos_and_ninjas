from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    desc = models.TextField()
class Ninja(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length=45)
    dojo_id = models.ForeignKey(Dojo, related_name="ninjas", on_delete= models.CASCADE)
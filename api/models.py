from django.db import models

# Create your models here.
class Group(models.Model):
    # unique = False allows for multiple groups with the same name
    name = models.CharField(max_length=50, null=False, unique=False)
    location = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=250, null=False, unique=False)
    
#    allows for group name to be repeated but not name and location
    class Meta:
        unique_together = (("name", "location"))

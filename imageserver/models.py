from django.db import models
from storages.backends.sftpstorage import SFTPStorage
SFS = SFTPStorage()

# Create your models here.
class ImageModel(models.Model):
    name = models.CharField(max_length=50)
    hour_accum = models.IntegerField()
    file = models.ImageField(upload_to='images', max_length=None)
    
    
    def __str__(self):
        return self.name

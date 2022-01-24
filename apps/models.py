from django.db import models

# Create your models here.

class Userurls(models.Model):
    inputurl=models.URLField()
    urlint=models.IntegerField(null=True)
    
    def __str__(self):
        return self.inputurl

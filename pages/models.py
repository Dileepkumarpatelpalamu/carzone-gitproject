from django.db import models

# Create your models here.

class Team (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    designation = models.CharField(max_length=50)
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateField()

    def __str__(self):
        return "%s %s %s %s %s"%(self.first_name,self.last_name,self.designation,self.twitter_link,self.created_date)

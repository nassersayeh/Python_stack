from django.db import models
import datetime

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['showtitle']) < 2:
            errors["showtitle"] = "Show Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Show Description should be at least 10 characters"
        if postData['releasedate'] >= str(datetime.date.fromisocalendar):
            errors["releasedate"] = "Show Release Date should be at least in the past"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=55)
    releasedate=models.DateField()
    desc = models.TextField()
    objects = BlogManager()




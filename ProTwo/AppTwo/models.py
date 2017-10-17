from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name #needed to show object models name

class WebUsers(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264)
    lname = models.CharField(max_length=264)
    email = models.CharField(max_length=264, unique=True)
    img = models.FileField(upload_to='webusers/', null=True)
    """
    img = models.FileField(upload_to='webusers/', null=True)
    First parameter tell's where to find imgs for that model
    And second, tell there's no obligation to have one, if there's no Images is ok
    """

    def __str__(self):
        return self.name

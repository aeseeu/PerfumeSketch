from django.db import models

class Post(models.Model) :
    title = models.TextField()
    image = models.ImageField()
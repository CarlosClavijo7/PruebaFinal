from django.db import models

class Post(models.Model):
    title = models.charField(max_length=255)
    content =models.TextFieldeld()
from django.db import models

# values of somthings in our website
class StuLinks(models.Model):
    link_name=models.CharField(max_length=255)
    link=models.URLField()


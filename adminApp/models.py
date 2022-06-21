from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ExampleModelTwo(models.Model):
    something = models.CharField(max_length=200)
class ExampleModel(models.Model):
    bool_example = models.BooleanField()
    small_text_example = models.CharField(max_length=100)
    large_text_example = models.TextField(max_length=1000)
    example_other_model_link = models.ForeignKey(to=ExampleModelTwo, on_delete=models.CASCADE)
class message(models.Model):
    inputField = models.TextField(max_length=100000000000000000000)
    To = models.ForeignKey(to=User, related_name="user_to", on_delete=models.CASCADE)
    From = models.ForeignKey(to=User, related_name="user_from", on_delete=models.CASCADE)

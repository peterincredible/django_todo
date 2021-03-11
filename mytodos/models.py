from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MyTodosModel(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(default="nothing")
    image = models.ImageField(upload_to="media/")
    datetime = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
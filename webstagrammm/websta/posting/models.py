from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class post(models.Model):
    user = models.ForeignKey(User,related_name="post",on_delete=CASCADE)
    image = models.ImageField(upload_to="images/",blank=True,null=True)
 
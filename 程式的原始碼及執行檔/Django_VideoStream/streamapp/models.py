from django.db import models
from django.utils import timezone
import django.utils.timezone as timezoneclass
# Create your models here.


# class Data(models.Model):
#     # host =
#     # topic =
#     id = models.AutoField(auto_created=True, primary_key=True)
#     local = models.CharField(max_length=50)
#     creatTime = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.creatTime

class data(models.Model):
    locals = models.CharField(max_length=50)
    creatTime = models.DateTimeField('更新時間', default=timezone.now())

    def __str__(self):
         return str(self.creatTime)

# class Message(models.Model):
#
#     # user=
#     data = models.ForeignKey(Data, on_delete=models.CASCADE)
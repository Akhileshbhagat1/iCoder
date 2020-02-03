from django.db import models


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return 'Message from  ' + self.name + '-' + self.email




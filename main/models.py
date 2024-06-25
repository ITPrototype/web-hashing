from django.db import models

class UserAccessLog(models.Model):
    ip_address = models.CharField(max_length=100)
    access_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ip_address} - {self.access_time}'

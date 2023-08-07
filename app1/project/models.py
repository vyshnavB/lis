from django.db import models

class login(models.Model):
    association_id = models.CharField(max_length=10)
    association_user_id = models.CharField(max_length=10)
    responseCode = models.IntegerField()
    message = models.CharField(max_length=100)

    def __str__(self):
        return f"Association ID: {self.association_id}, User ID: {self.association_user_id}, Response Code: {self.responseCode}, Message: {self.message}"

from django.db import models

class UserProfile(models.Model):
    username = models.CharField()
    password = models.CharField(max_length=50)
    email = models.EmailField()
    last_name = models.CharField()
    first_name = models.CharField()


    def __str__(self):
        return self.username
    
    def say_hello(self):
        return f"Hello {self.first_name} {self.last_name}"
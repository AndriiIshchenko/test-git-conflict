from django.db import models

class UserProfile(models.Model):
    username = models.CharField()
    password = models.CharField(max_length=120)
    email = models.EmailField()
    first_name = models.CharField()


    def __str__(self):
        return self.username
    
    def get_full_name(self) -> str:
        return self.first_name + "gav"

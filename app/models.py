from django.db import models

class User(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    create_timestamp = models.CharField(max_length=100)
    update_timestamp = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)




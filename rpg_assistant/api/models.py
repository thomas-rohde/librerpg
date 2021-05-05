from django.db import models
import string
import random

def generate_unique_code():
    lenght = 10

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=lenght))
        if Room.objects.filter(code=code).count() == 0:
            break
    
    return code

# Create your models here.

class Room(models.Model):
    code = models.CharField(max_lenght=8, default="", unique=True) #making the room unique, 
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1) #votes to skip the music
    created_at = models.DateTimeField(auto_now_add=True)

    #def is_host_this():

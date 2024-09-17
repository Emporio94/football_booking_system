from django.db import models
from datetime import datetime

# Create your models here.

class Players(models.Model):
    username = models.CharField(max_length=24)
    phone_number = models.CharField(max_length=24, name="phone_number")

    class Meta:
        verbose_name_plural = "Players"

    def __str__(self) -> str:
        return self.username
    
class PlayerList(models.Model):
    game_week = models.IntegerField(primary_key=True)
    players = models.ManyToManyField('Players')  
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        current_week = datetime.now().isocalendar()[1]  # Get the current week of the year
        self.game_week = current_week  # Set the game week as the current week
        super(PlayerList, self).save(*args, **kwargs)


    def __str__(self):
        return f"Player List for Game Week {self.game_week}"
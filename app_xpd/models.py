from django.db import models
from app_manage.models import Lineup, Role, Position, Managing
# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=300, blank=True)
    image_link = models.TextField(blank=True)
    image = models.ImageField(upload_to="static/assets/media", blank=True)

    def __str__(self):
        return self.title



class Member(models.Model):
    in_game_name = models.CharField(max_length=20, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role")
    second_role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True, related_name="second_role")
    image = models.ImageField(upload_to="media/members", default='default/logo.png')
    lineup = models.ForeignKey(Lineup, on_delete=models.CASCADE, null=True)
    position_in_clan = models.ForeignKey(Managing, on_delete=models.CASCADE, related_name="position_in_clan", null=True, blank=True)
    managing_position = models.ForeignKey(Managing, on_delete=models.CASCADE, related_name="managing_position", blank=True, null=True)

    def __str__(self):
        return f"{self.in_game_name} | {self.role}/{self.managing_position}"


class User(models.Model):
    in_game_name = models.CharField(max_length=20, unique=True)
    clan_name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True, blank=False, max_length=50)
    phone_number = models.CharField(unique=True, blank=True, max_length=10)
    password = models.CharField(blank=False, max_length=25)
    position_in_clan = models.ForeignKey(Position, on_delete=models.CASCADE, null=False, default=3)
    image = models.ImageField(upload_to="media/users", default='default/logo.png')
    

    def __str__(self):
        return f"{self.in_game_name} | {self.clan_name}"



from django.contrib import admin
from .models import Announcement, Member, Lineup, Role, Position, Managing , User
# Register your models here.
admin.site.register(Announcement)
admin.site.register(User)
admin.site.register(Member)
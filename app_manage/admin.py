from django.contrib import admin
from .models import Lineup, Role, Position, Managing
# Register your models here.
admin.site.register(Lineup)
admin.site.register(Role)
admin.site.register(Position)
admin.site.register(Managing)
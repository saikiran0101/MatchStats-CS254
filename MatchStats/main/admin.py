from django.contrib import admin

from .models import Team, Player, Stadium, Match, Transfer, Goal, Staff

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Stadium)
admin.site.register(Match)
admin.site.register(Transfer)
admin.site.register(Goal)
admin.site.register(Staff)
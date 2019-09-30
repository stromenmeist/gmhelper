from django.contrib import admin
from .models import Adventure, Milestone


class AdventureAdmin(admin.ModelAdmin):
    pass


class MilestoneAdmin(admin.ModelAdmin):
    pass

admin.site.register(Adventure, AdventureAdmin)
admin.site.register(Milestone, MilestoneAdmin)

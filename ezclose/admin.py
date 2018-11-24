# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from ezclose.models import UserProfile, Realtor, Client, Transactions, Tasks, Activity, Milestone, DefaultTasks, DefaultMilestones, Brokerage, Property, Team, TeamMember

#class TasksAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug':('name',)}

class TransactionsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('status',)} 
    readonly_fields = ('id',)

      
admin.site.register(Realtor)
admin.site.register(Client)
#admin.site.register(Transactions)
admin.site.register(Tasks)
admin.site.register(Activity)
admin.site.register(UserProfile)
admin.site.register(Milestone)
admin.site.register(DefaultTasks)
admin.site.register(DefaultMilestones)
admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(Brokerage)
admin.site.register(Property)
admin.site.register(Team)
admin.site.register(TeamMember)

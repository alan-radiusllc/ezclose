# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from ezclose.models import UserProfile, Realtor, Client, Transactions, Tasks, Activity, Milestone, DefaultTasks, DefaultMilestones

#class TasksAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug':('name',)}

class TransactionsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('status',)} 
      
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


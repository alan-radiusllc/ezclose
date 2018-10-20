# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from ezclose.models import Realtor, Client, Transactions, Tasks, Activity

admin.site.register(Realtor)
admin.site.register(Client)
admin.site.register(Transactions)
admin.site.register(Tasks)
admin.site.register(Activity)




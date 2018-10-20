# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Realtor(models.Model):    
    # add ForeignKey to User table
    name       = models.CharField(max_length=128)
    brokerage  = models.CharField(max_length=128) # make this a foreign key
    street     = models.CharField(max_length=128) #   and this
    city       = models.CharField(max_length=128) #   and this
    zipcode    = models.IntegerField()            #   and this
    phone1     = models.CharField(max_length=20)  #   and one phone
    phone2     = models.CharField(max_length=20)
    phone1Type = models.CharField(max_length=8)
    phone2Type = models.CharField(max_length=8)
    email      = models.EmailField(max_length=254, unique=True)
    # fax
    # local branch - will provide locality - part of foreign key?
    # pager
    # more phones
    # assistant / admin point of contact
    
    def __str__(self):
        return self.name
      
    def __unicode__(self):
        return self.name
        
class Client(models.Model):
    name        = models.CharField(max_length=128)
    street      = models.CharField(max_length=128)
    city        = models.CharField(max_length=128)
    zipcode     = models.IntegerField()
    phone1      = models.CharField(max_length=20)
    phone2      = models.CharField(max_length=20)
    phone1Type  = models.CharField(max_length=8)
    phone2Type  = models.CharField(max_length=8)
    email       = models.EmailField(max_length=254, unique=True)
    newCustomer = models.BooleanField() # if this is the first transaction
    
    def __str__(self):
        return self.name
      
    def __unicode__(self):
        return self.name
         
class Transactions(models.Model):
	realtor         = models.ForeignKey(Realtor)
	client          = models.ForeignKey(Client)
	transactionType = models.CharField(max_length=20)
	property        = models.CharField(max_length=20)  # the MLS number? 
	status          = models.CharField(max_length=8)
	active          = models.BooleanField()
	startDate       = models.DateTimeField()
	endDate         = models.DateTimeField()
	lastActivity    = models.DateTimeField()
	# team          = models.ForeignKey(Team)  # add when Team class is ready
	
	def __str__(self):
	    return (self.client.name, self.startDate)
	    
	def __unicode__(self):
	    return (self.client.name, self.startDate)
	
	class Meta:
	    ordering = ["startDate"]
	    verbose_name_plural = 'Transactions'
    
class Tasks(models.Model):
    transaction   = models.ForeignKey(Transactions)
    name          = models.CharField(max_length=128)
    group         = models.CharField(max_length=128)
    category      = models.CharField(max_length=128)
    wbs           = models.IntegerField()
    prerequisites = models.NullBooleanField() # eventually make this a many to many
    ripeDate      = models.DateTimeField()
    dueDate       = models.DateTimeField()
    status        = models.CharField(max_length=8)
    dependents    = models.NullBooleanField() # eventually make many to many
    assignee      = models.ForeignKey(Client) # make this to User table
    milestone     = models.CharField(max_length=128, default='None')  # link to Milestone?
    beforeAfter   = models.NullBooleanField()
    overDue       = models.NullBooleanField()  # computed based on milestone and date?
    
    def __str__(self):
        return self.name
      
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = 'Tasks'
        
class Milestone(models.Model):
    transaction   = models.ForeignKey(Transactions)
    name = models.CharField(max_length=128, unique=True)
    date = models.DateTimeField()
    type = models.CharField(max_length=128) # meeting, filing, approval
    scheduled = models.NullBooleanField()
    def __str__(self):
        return self.task.name
      
    def __unicode__(self):
        return self.task.name
        
class Activity(models.Model):
    task      = models.ForeignKey(Tasks)
    timestamp = models.DateTimeField()
    actor     = models.ForeignKey(Client) # make this to User table
    action    = models.CharField(max_length=8) # foreign key to actions table?
    
    def __str__(self):
        return self.task.name
      
    def __unicode__(self):
        return self.task.name
        
    class Meta:
        verbose_name_plural = 'Activity'

# This class holds the default tasks, where the tags are things like: Default,
#   short, FHA, HasRadon, NeedsSepticInspection, etc.
# When starting a new Transaction, copy the appropriate rows from this table
#   into the Tasks table with the new Transaction ID
class DefaultTasks(models.Model):
    name          = models.CharField(max_length=128, unique=True)
    purchase      = models.NullBooleanField()   # buy or sell
    locality      = models.CharField(max_length=128)  # can help differentiate
    brokerage     = models.CharField(max_length=128)  # make this a foreign key to table
    tag1          = models.CharField(max_length=128)  # make these selection? or foreign keys?
    tag2          = models.CharField(max_length=128)
    tag3          = models.CharField(max_length=128)

    group         = models.CharField(max_length=128)
    category      = models.CharField(max_length=128)
    wbs           = models.IntegerField()     # how to represent 
    prerequisites = models.NullBooleanField() # eventually make this a many to many
    dependents    = models.NullBooleanField() # eventually make many to many
    assignee      = models.ForeignKey(Client) # make this to User table
    milestone     = models.CharField(max_length=128) # foreign key to milestone table
    milestoneDate = models.DateTimeField() # 3NF?
    beforeAfter   = models.NullBooleanField()

    def __str__(self):
        return self.task.name
      
    def __unicode__(self):
        return self.task.name
        
    class Meta:
        verbose_name_plural = 'DefaultTasks'

class DefaultMilestones(models.Model):
	name  = models.CharField(max_length=128, unique=True)
	type = models.CharField(max_length=128) # meeting, filing, approval
	
	def __str__(self):
		return self.task.name
	
	def __unicode__(self):
		return self.task.name

	class Meta:
		verbose_name_plural = 'DefaultMilestones'

#class Team()

#class TeamMembers()

#class Realtors()
#class MortgageBrokers()
#class Lenders()
#class Closings()
#class Attorneys()
#class Bankers()
#class Insurance()
#class Inspectors()
#class Specialty()
#class HomeRepair()
#class Roofers()
#class Windows()

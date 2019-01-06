# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from smart_selects.db_fields import ChainedForeignKey

# Variables for Choices
CELL = "CELL"
OFFICE = "OFFICE"
HOME = "HOME"
ADMIN = "ADMIN"
PHONE_CHOICES = ( (CELL, "cell"), (OFFICE, "office"), (HOME, "home"), (ADMIN, "admin"), )

BUY = "BUY"
SELL = "SELL"
SELL_BUY = "SELL_BUY"
TRANSACTION_TYPES = ( (BUY, "buy"), (SELL, "sell"), (SELL_BUY, "sell / buy"), )

MEETING = "MEETING"
RESEARCH = "RESEARCH"
DOCUMENTS = "DOCUMENTS"
ADMIN = "ADMIN"
CALL = "CALL"
EMAIL = "EMAIL"
INFO_REVIEW = "INFO_REVIEW"
VENDOR = "VENDOR"
TASK_TYPES = ((MEETING, "Meeting"), (RESEARCH, "Research"), (DOCUMENTS, "Documents"),
              (ADMIN, "Administrative"), (CALL, "Phone Call"), (EMAIL, "Email"),
              (INFO_REVIEW, "Information Review"), (VENDOR, "Vendor Action"),)

MILESTONE_TYPES = ((MEETING, "Meeting"), (DOCUMENTS, "Documents"), (ADMIN, "Administrative"),)

# task groups

NOT_READY = "NOT_READY"
READY     = "READY"
DUE_ON    = "DUE_ON"
DUE       = "DUE"
OVERDUE   = "OVERDUE"
CRITICAL  = "CRITICAL"
STARTED   = "STARTED"
COMPLETE  = "COMPLETE"
TASK_STATUS = ((NOT_READY, "Not Ready"), (READY, "Ready"), (DUE_ON, "Due On"),
              (DUE, "Due"), (OVERDUE, "Overdue"), (CRITICAL, "Critical"), 
              (STARTED, "Started"), (COMPLETE, "Complete"),)


# transaction status

INITIAL = "INITIAL"
ACTIVE = "ACTIVE"
COMPLETE = "COMPLETE"
INACTIVE = "INACTIVE"
ABANDONED = "ABANDONED"
TRANSACTION_STATUS = ((INITIAL, "Initial"), (ACTIVE, "Active"), (COMPLETE, "Complete"),
                      (INACTIVE, "Inactive"), (ABANDONED, "Abandoned"))
# activity actions

CONVENTIONAL = "CONVENTIONAL"
JUMBO = "JUMBO"
SHORT = "SHORT"
VA = "VA"
FHA = "FHA"
FORECLOSURE = "FORECLOSURE"
FINANCE_TYPES = ( (CONVENTIONAL, "Conventional"),
                  (JUMBO,        "Jumbo"),
                  (SHORT,        "Short"),
                  (VA,           "VA"),
                  (FHA,          "FHA"),
                  (FORECLOSURE,  "Foreclosure"), )

NORMAL = "NORMAL"
SHORT_SELL = "SHORT_SELL"
FORECLOSE = "FORECLOSE"
SELL_TYPES = ( (NORMAL, "Normal"),
               (SHORT_SELL, "Short Sell"),
               (FORECLOSE,  "Foreclosure"), )

BEFORE = "BEFORE"
AFTER  = "AFTER"
COINCIDENT = "COINCIDENT"
NO_RELATION  = "NO_RELATION"
RELATIONSHIPS = ((BEFORE, "Before"), (AFTER, "AFTER"), (COINCIDENT, "Coincident"), 
                 (NO_RELATION, "No Relationship"), )
                                                  
RADON = "RADON"
TITLE_5 = "TITLE_5"
SHORT = "SHORT"
SPECIAL_INSP = "SPECIAL_INSP"
OTHER = "OTHER"

TAGS = ((RADON, "Radon"), (TITLE_5, "Title V"), (SHORT, "SHORT"),
        (SPECIAL_INSP, "Special Inspection"), (OTHER, "Other"), )

# sfh, townhouse, condo, duplex,
HOME = "SFH"
TOWNHOME = "TOWNHOME"
CONDO = "CONDO"
DUPLEX = "DUPLEX"
PROPERTY_TYPES = ((HOME, "Single Family Home"), (TOWNHOME, "Townhouse"), (CONDO, "Condominium"),
                  (DUPLEX, "Duplex"),)
                         
# Create your models here.

# This adds fields to the standard User fields
# Note that users will be of different type: Client, Realtor, System Admin, Lender, etc.
class Brokerage(models.Model):
    name       = models.CharField(max_length=128)
    street     = models.CharField(max_length=128, blank=True, null=True)
    city       = models.CharField(max_length=128, blank=True, null=True)
    zipcode    = models.CharField(max_length=128, blank=True, null=True)
    phone1     = models.CharField(max_length=20, blank=True, null=True)  
    phone2     = models.CharField(max_length=20, blank=True, null=True)
    manager	   = models.CharField(max_length=128, blank=True, null=True)
    mngrphone  = models.CharField(max_length=20, blank=True, null=True)
    mngremail  = models.EmailField(max_length=254, blank=True, null=True)
    locality   = models.CharField(max_length=128, blank=True, null=True, default='')
    parent     = models.ForeignKey('self', blank=True, null=True) # if a local branch of another
    def __str__(self):
        return self.name
        
    def __unicode__(self):
        return self.name
        

class Property(models.Model):
    mls         = models.CharField(max_length=20, unique=True, blank=True, null=True)
    street      = models.CharField(max_length=128, blank=True, null=True)
    street2     = models.CharField(max_length=128, blank=True, null=True)
    city        = models.CharField(max_length=128, blank=True, null=True)
    zipcode     = models.IntegerField(blank=True, null=True)
    type        = models.CharField(max_length=20, choices = PROPERTY_TYPES, blank=True, null=True)  
    picture     = models.ImageField(upload_to='profile_images', blank=True, null=True)
    
    def __str__(self):
        return self.mls
        
    def __unicode__(self):
        return self.mls
        
    class Meta:
        verbose_name_plural = 'Properties'
        
        
class Realtor(models.Model):    
    user       = models.ForeignKey(User)
    name       = models.CharField(max_length=128) # required
    brokerage  = models.ForeignKey(Brokerage, blank=True, null=True) 
    phone1     = models.CharField(max_length=20)  # required
    phone2     = models.CharField(max_length=20, blank=True, null=True)
    phone1Type = models.CharField(max_length=8, choices=PHONE_CHOICES, blank=True, null=True) # make choice: cell, work, home
    phone2Type = models.CharField(max_length=8, choices=PHONE_CHOICES, blank=True, null=True)
    email      = models.EmailField(max_length=254, unique=True) # required
    # fax
    # pager
    # more phones
    # assistant / admin point of contact
    
    def __str__(self):
        return self.name
      
    def __unicode__(self):
        return self.name
        
class Client(models.Model):
    user        = models.ForeignKey(User)
    name        = models.CharField(max_length=128) # required
    street      = models.CharField(max_length=128, blank=True, null=True)
    street2     = models.CharField(max_length=128, blank=True, null=True)
    city        = models.CharField(max_length=128, blank=True, null=True)
    zipcode     = models.IntegerField(blank=True, null=True)
    phone1      = models.CharField(max_length=20) # required
    phone2      = models.CharField(max_length=20, blank=True, null=True)
    phone1Type  = models.CharField(max_length=8, choices=PHONE_CHOICES, blank=True, null=True)
    phone2Type  = models.CharField(max_length=8, choices=PHONE_CHOICES, blank=True, null=True)
    email       = models.EmailField(max_length=254, unique=True) # required
    newCustomer = models.BooleanField() # if this is the first transaction
    
    def __str__(self):
        return self.name
      
    def __unicode__(self):
        return self.name
         
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name        = models.CharField(max_length=128) # required
    picture     = models.ImageField(upload_to='profile_images', blank=True, null=True)
    website     = models.URLField(blank=True, null=True)
    street      = models.CharField(max_length=128, blank=True, null=True)
    street2     = models.CharField(max_length=128, blank=True, null=True)
    city        = models.CharField(max_length=128, blank=True, null=True)
    zipcode     = models.IntegerField(blank=True, null=True)
    phone1      = models.CharField(max_length=20) # required
    phone2      = models.CharField(max_length=20, blank=True, null=True)
    phone1Type  = models.CharField(max_length=8, choices=PHONE_CHOICES, blank=True, null=True)
    phone2Type  = models.CharField(max_length=8, choices=PHONE_CHOICES, blank=True, null=True)
    isRealtor   = models.BooleanField(default=False)
    brokerage   = models.ForeignKey(Brokerage, blank=True, null=True)
    myRealtor   = models.ForeignKey(Realtor, blank=True, null=True)

    def __str__(self):
        return self.user.username
        
    def __unicode__(self):
        return self.user.username

class Transactions(models.Model):
    realtor         = models.ForeignKey(Realtor)
    client          = models.ForeignKey(Client)
    transactionType = models.CharField(max_length=20, choices=TRANSACTION_TYPES) 
    property        = models.ForeignKey(Property, blank=True, null=True) 
    status          = models.CharField(max_length=10, choices=TRANSACTION_STATUS)
    active          = models.BooleanField() # redundant?
    startDate       = models.DateTimeField()
    endDate         = models.DateTimeField(blank=True, null=True)
    lastActivity    = models.DateTimeField(blank=True, null=True)
    # team          = models.ForeignKey(Team)  # add when Team class is ready
    slug            = models.SlugField(unique=True)
    # tags? Use these here to indicate which ones we need from the Default tasks?
    tag1            = models.CharField(max_length=12, choices=TAGS, blank=True, null=True)
    tag2            = models.CharField(max_length=12, choices=TAGS, blank=True, null=True)
    tag3            = models.CharField(max_length=12, choices=TAGS, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        tstr = self.startDate.strftime('%m_%d_%Y__%H_%M_%S')
        self.slug = slugify(self.client.name + tstr)
        #self.slug = slugify(self.client.name+ "%d" % self.id)
        super(Transactions, self).save(*args, **kwargs)
    
    def __str__(self):
        str = "%s %s %d" % (self.client.name, self.startDate, self.id)
        #str = "%s_%s_%s" % (self.client.name, self.realtor.name, str(self.id))
        return str
        
    def __unicode__(self):
        str = "%s %s %d" % (self.client.name, self.startDate, self.id)
        return str

    class Meta:
        ordering = ["startDate"]
        verbose_name_plural = 'Transactions'

class Milestone(models.Model):
    transaction = models.ForeignKey(Transactions)
    name        = models.CharField(max_length=128, unique=True)
    date        = models.DateTimeField(blank=True, null=True)
    type        = models.CharField(max_length=128, choices=MILESTONE_TYPES) # meeting, filing, approval
    scheduled   = models.NullBooleanField() # or use status?
    def __str__(self):
        return self.name
      
    def __unicode__(self):
        return self.name

# This table is all tasks for all transactions in the database            
class Tasks(models.Model):
    transaction   = models.ForeignKey(Transactions)
    name          = models.CharField(max_length=128)  # need to generate a unique name per transaction for the slug
    group         = models.CharField(max_length=128, blank=True, null=True) # choice
    category      = models.CharField(max_length=25, choices=TASK_TYPES, blank=True, null=True) # choice
    wbs           = models.IntegerField(blank=True, null=True) # ?
    prerequisites = models.NullBooleanField(blank=True, null=True) # eventually make this a many to many to self table
    ripeDate      = models.DateTimeField(blank=True, null=True)
    dueDate       = models.DateTimeField(blank=True, null=True)
    status        = models.CharField(max_length=10, choices=TASK_STATUS, blank=True, null=True) # choice
    dependents    = models.NullBooleanField(blank=True, null=True) # eventually make many to many to self?
    assignee      = models.ForeignKey(User) # restrict to the team, usually client or realtor
    milestone     = models.ForeignKey(Milestone, blank=True, null=True) # optional, if this task is a milestone
    beforeAfter   = models.NullBooleanField(blank=True, null=True) # choice? This should probably be in milestone table?
    overDue       = models.NullBooleanField()  # computed based on milestone and date? redundant with status
    slug          = models.SlugField(unique=True)
    
    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.name)
    #    super(Tasks, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
      
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = 'Tasks'
        
# This table will hold the record of when changes to the tasks are made
class Activity(models.Model):
    task      = models.ForeignKey(Tasks)
    timestamp = models.DateTimeField()
    actor     = models.ForeignKey(Client) # make this to User table
    action    = models.CharField(max_length=8) # foreign key to actions table? choice?
    
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
    purchase      = models.CharField(max_length=8, choices=TRANSACTION_TYPES, blank=True, null=True)
    locality      = models.CharField(max_length=128, blank=True, null=True)  # can help differentiate
    brokerage     = models.CharField(max_length=128, blank=True, null=True)  # make this a foreign key to table
    tag1          = models.CharField(max_length=12, choices=TAGS, blank=True, null=True)  # make these selection? or foreign keys?
    tag2          = models.CharField(max_length=12, choices=TAGS, blank=True, null=True)
    tag3          = models.CharField(max_length=12, choices=TAGS, blank=True, null=True)

    group         = models.CharField(max_length=128, blank=True, null=True)
    category      = models.CharField(max_length=128, blank=True, null=True)
    wbs           = models.IntegerField(blank=True, null=True)     # how to represent 
    prerequisites = models.NullBooleanField() # eventually make this a many to many
    dependents    = models.NullBooleanField() # eventually make many to many
    assignee      = models.ForeignKey(User, blank=True, null=True) # make this to User table
    milestone     = models.CharField(max_length=128, blank=True, null=True) # foreign key to milestone table
    milestoneDate = models.DateTimeField(blank=True, null=True) # 3NF?
    beforeAfter   = models.NullBooleanField()

    def __str__(self):
        return self.name
      
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = 'DefaultTasks'

# These are default milestone tasks that can be loaded into the Milestone table when a transaction is started
class DefaultMilestones(models.Model):
    name  = models.CharField(max_length=128, unique=True)
    type = models.CharField(max_length=128, blank=True, null=True) # make choice: meeting, filing, approval
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'DefaultMilestones'


#class TeamType(models.Model):
REALTOR = "REALTOR"
REAL_ESTATE_BROKER  = "REAL_ESTATE_BROKER"
LENDER  = "LENDER"
MORTGAGE_BROKER = "MORTGAGE_BROKER"
CLOSING = "CLOSING"
ATTORNEY = "ATTORNEY"
BANKER = "BANKER"
INSURANCE = "INSURANCE"
INSPECTOR = "INSPECTOR"
SPECIALTY_INSPECTOR = "SPECIALTY_INSPECTOR"
HOME_REPAIR = "HOME_REPAIR"
CONTRACTOR = "CONTRACTOR"
WARRANTY = "WARRANTY"
OTHER = "OTHER"

TEAM_TYPES = ((REALTOR, "Realtor"),
              (REAL_ESTATE_BROKER, "Real Estate Broker"),
              (LENDER, "Lender"),
              (MORTGAGE_BROKER, "Mortgage Broker"),
              (BANKER, "Banker"),
              (CLOSING, "Closing"),
              (ATTORNEY, "Attorney"),
              (INSURANCE, "Home Owners Insurance"),
              (INSPECTOR, "Home Inspector"),
              (SPECIALTY_INSPECTOR, "Speialty Inspector"),
              (HOME_REPAIR, "Home Repair"),
              (CONTRACTOR, "Contractor"),
              (WARRANTY, "Home Warranty"),
              (OTHER, "Other"),)

class TeamType(models.Model):
    type       = models.CharField(max_length=25, choices=TEAM_TYPES)
    def __str__(self):
        return self.type

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'TeamTypes'
                  
class TeamMember(models.Model):
    type       = models.ForeignKey('TeamType', related_name="name")
    company    = models.CharField(max_length=128)
    name       = models.CharField(max_length=128) # the point of contact
    street     = models.CharField(max_length=128, blank=True, null=True)
    city       = models.CharField(max_length=128, blank=True, null=True)
    zipcode    = models.CharField(max_length=128, blank=True, null=True)
    phone1     = models.CharField(max_length=20, blank=True, null=True)  
    phone2     = models.CharField(max_length=20, blank=True, null=True)
    manager	   = models.CharField(max_length=128, blank=True, null=True)
    mngrphone  = models.CharField(max_length=20, blank=True, null=True)
    mngremail  = models.EmailField(max_length=254, blank=True, null=True)
    locality   = models.CharField(max_length=128, blank=True, null=True, default='')
    parent     = models.ForeignKey('self', blank=True, null=True) # if a local branch of another

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'TeamMembers'

class Team(models.Model):
    transaction = models.ForeignKey(Transactions)
    # client      = models.ForeignKey(Client)       # Do we want to do teams by client or by transaction?
    member      = models.ForeignKey(TeamMember)
    type        = models.ForeignKey(TeamType, null=True)
    dateAdded   = models.DateTimeField(blank=True, null=True)
    dateChanged = models.DateTimeField(blank=True, null=True)
    modified    = models.IntegerField(default=0)

    def __str__(self):
        return self.transaction.slug

    def __unicode__(self):
        return self.transaction.slug

    class Meta:
        verbose_name_plural = 'Teams'

    
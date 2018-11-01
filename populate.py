import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ez1.settings')
  
import django
django.setup()

from ezclose.models import Client, Realtor, DefaultTasks, DefaultMilestones
from ezclose.models import Transactions, Tasks, Milestone, Activity, UserProfile
# from ezclose.User import User
from django.contrib.auth.models import User
  
def populate(howMuch):
    # users
    for i in range(21,30):
        userstr = 'John%dSmith' % i
        print userstr
        nuser = User.objects.create(username=userstr)
        nuser.first_name = 'John%d' % i
        nuser.last_name = 'Smith%d' % i 
        estr = 'test%d@ezclose.net' % i
        nuser.email = estr
        nuser.set_password('demo')
        nuser.save()
        phonestr = '70355512%d' % i
        
        if i % 3 == 0 or i % 3 == 1:
            client = Client.objects.create(user=nuser,name=userstr,phone1=phonestr,email=estr,newCustomer=True)
            # client.phone1 = '57128627%d' % i
            #client.email = 'test%d@ezclose.net' % i
            #client.newCustomer = True
            client.street = 'Maple%d' % i
            client.save()
            
        else:
            nuser.name = 'Joan%dPublic' % i
            nuser.save()
            realtor = Realtor.objects.create(user=nuser,name=userstr,phone1=phonestr,email=estr)
            realtor.street = 'Elm%d' % i
            realtor.save()
            
            
     ''''
     # DefaultTasks
     class DefaultTasks(models.Model):
     name          = models.CharField(max_length=128, unique=True)
     purchase      = models.NullBooleanField()   # buy or sell - make this a choice
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
     beforeAfter   = models.NullBooleanField
     ''''
     #  make a list of tasks for a purchase from a certain brokerage so just need the name, group/category, assignee,   
    
     # DefaultMilestones
    
     #if howMuch == 'all':
        # Transactions
        
        # Tasks
        
        # Milestones
        
        # Activity
        
	
if __name__ == '__main__':
    print ("Staring populate script")
    populate('all')  # could be 'base'
    
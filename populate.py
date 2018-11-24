import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ez1.settings')
  
import django
django.setup()

from ezclose.models import Client, Realtor, DefaultTasks, DefaultMilestones, Brokerage
from ezclose.models import Transactions, Tasks, Milestone, Activity, UserProfile, Property
# from ezclose.User import User
from django.contrib.auth.models import User
  
def addDefTask(name, purchase, locality, tag1, group, category, wbs, assignee, points):
    # Note: add points to default task list
    dtask = DefaultTasks.objects.get_or_create(name=name,purchase=purchase,locality=locality,
             tag1=tag1,group=group,category=category,wbs=wbs)[0]
    dtask.save()
    return dtask
            
def populate(howMuch):
    # users
    for i in range(41,30):
        userstr = 'John%dSmith' % i
        print userstr
        nuser = User.objects.get_or-create(username=userstr)
        nuser.first_name = 'John%d' % i
        nuser.last_name = 'Smith%d' % i 
        estr = 'test%d@ezclose.net' % i
        nuser.email = estr
        nuser.set_password('demo')
        nuser.save()
        phonestr = '70355512%d' % i
        
        if i % 3 == 0 or i % 3 == 1:
            client = Client.objects.get_or_create(user=nuser,name=userstr,phone1=phonestr,email=estr,newCustomer=True)
            # client.phone1 = '57128627%d' % i
            #client.email = 'test%d@ezclose.net' % i
            #client.newCustomer = True
            client.street = 'Maple%d' % i
            client.save()
            
        else:
            nuser.name = 'Joan%dPublic' % i
            nuser.save()
            realtor = Realtor.objects.get_or_create(user=nuser,name=userstr,phone1=phonestr,email=estr)
            realtor.street = 'Elm%d' % i
            realtor.save()
 
        
    # Brokerages
    bname       = 'Real Realty'
    bstreet     = '111 Chain Bridge Ave.'
    bcity       = 'Boston, MA'
    bzipcode    = '02150'
    bphone1     = '5084771495'
    bmanager	= 'Martha E. Smith'
    bmngrphone  = '5084771912'
    bmngremail  = 'martha@realr.com'
    blocality   = 'MA'
    broke = Brokerage.objects.get_or_create(name=bname,street=bstreet,city=bcity,zipcode=bzipcode,
                 phone1=bphone1,manager=bmanager,mngrphone=bmngrphone,mngremail=bmngremail,
                 locality=blocality)[0]
    broke.save()
    
    bname       = 'Long and Foster'
    bstreet     = '5 Foster St.'
    bcity       = 'Brockton, MA'
    bzipcode    = '02549'
    bphone1     = '5084771495'
    bmanager	= 'Steve Foster'
    bmngrphone  = '5084771919'
    bmngremail  = 'steve@landf.com'
    blocality   = 'MA'
    broke = Brokerage.objects.get_or_create(name=bname,street=bstreet,city=bcity,zipcode=bzipcode,
                 phone1=bphone1,manager=bmanager,mngrphone=bmngrphone,mngremail=bmngremail,
                 locality=blocality)[0]
    broke.save()
       
    bname       = 'AAA Realty'
    bstreet     = '280 Warren Ave.'
    bcity       = 'Hudson, MA'
    bzipcode    = '02559'
    bphone1     = '5084771494'
    bmanager	= 'Charles Xavier'
    bmngrphone  = '5084771911'
    bmngremail  = 'charles@aaar.com'
    blocality   = 'MA'
    bparent     = broke
    broke2 = Brokerage.objects.get_or_create(name=bname,street=bstreet,city=bcity,zipcode=bzipcode,
                 phone1=bphone1,manager=bmanager,mngrphone=bmngrphone,mngremail=bmngremail,
                 locality=blocality)[0]
    broke2.save()
    
    
    # Properties
    propmls = 1009998887
    propstreet = '123 Main St.'
    propcity = 'McLean'
    propzip = 22101
    proptype = 'Single Family Home'
    prop = Property.objects.get_or_create(mls=propmls,street=propstreet,city=propcity,zipcode=propzip,
            type=proptype)[0]
    prop.save()
    
    propmls = 2001001001
    propstreet = '857 Woodchuck Rd.'
    prop = Property.objects.get_or_create(mls=propmls,street=propstreet,city=propcity,zipcode=propzip,
            type=proptype)[0]
    prop.save()

    propmls = 3334445556
    propstreet = '111 Park Dr.'
    prop = Property.objects.get_or_create(mls=propmls,street=propstreet,city=propcity,zipcode=propzip,
            type=proptype)[0]
    prop.save()

    propmls = 1112223331
    propstreet = '84520 My St.'
    prop = Property.objects.get_or_create(mls=propmls,street=propstreet,city=propcity,zipcode=propzip,
            type=proptype)[0]
    prop.save()

    propmls = 1231231234
    propstreet = '11 Goat Way'
    prop = Property.objects.get_or_create(mls=propmls,street=propstreet,city=propcity,zipcode=propzip,
            type=proptype)[0]
    prop.save()

    propmls = 72398159
    propstreet = '235 Lincoln St.'
    propcity = 'Seekonk, MA'
    propzip = 02771
    proptype = 'Single Family Home'
    prop = Property.objects.get_or_create(mls=propmls,street=propstreet,city=propcity,zipcode=propzip,
            type=proptype)[0]       
    prop.save()

    propmls = 1201625
    propstreet = '19 Rye St.'
    propcity = 'Seekonk, MA'
    propzip = 02771
    proptype = 'Single Family Home'
    prop = Property.objects.get_or_create(mls=propmls,street=propstreet,city=propcity,zipcode=propzip,
            type=proptype)[0]           
    prop.save()


    ## Buy Home Tasks
  
    #addDefTaskRollup('BUY HOME','BUY','ALL','',1)
    #addDefTaskRollup('RESEARCH/PREP','BUY','ALL','',2)
    addDefTask('Pre-Rep Appt',            'BUY','ALL','','RESEARCH/PREP','MEETING',    3,'BOTH',2) # point to rollup task
    addDefTask('Sign Buyer Rep Agreement','BUY','ALL','','RESEARCH/PREP','DOCUMENTS',  3,'BOTH',2)
    addDefTask('Pre-approval letter',     'BUY','ALL','','RESEARCH/PREP','VENDOR',     3,'CLIENT',3)
    addDefTask('Verify Pre-approval',     'BUY','ALL','','RESEARCH/PREP','INFO_REVIEW',3,'AGENT',1)

    #addDefTaskRollup('PROPERTY RESEARCH',True,'ALL','',2)
    addDefTask('Research potential properties', 'BUY','ALL','','PROPERTY RESEARCH','RESEARCH', 3, 'AGENT',2)
    addDefTask('Identify Homes of Interest', 'BUY', 'ALL', '', 'PROPERTY RESEARCH','MEETING', 3, 'BOTH',2)
    addDefTask('Develop Plan to Visit Homes','BUY', 'ALL', '', 'PROPERTY RESEARCH','RESEARCH',3,'BOTH',2)
    addDefTask('Visit Homes of Interest','BUY','ALL','','PROPERTY_RESEARCH','MEETING',3,'BOTH',10)
    addDefTask('Downselect Prospective Properties','BUY','ALL','','PROPERTY_RESEARCH','MEETING',3,'BOTH',3)

    #addDefTaskRollup('RESEARCH EACH PROSPECTIVE PROPERTY',True,'ALL','',2)
    addDefTask('Research Tax, Public Records, Etc.', 'BUY', 'ALL', '', 'RESEARCH PROSPECTIVE PROPERTY', 'RESEARCH', 3, 'AGENT',2)
    addDefTask('Research Property Restrictions, Conditions, Appraisal, Needed Repairs', 'BUY', 'ALL', '', 'RESEARCH PROSPECTIVE PROPERTY', 'RESEARCH', 3, 'AGENT',2)
    addDefTask('Identify and Verify HOA Documents and Fees', 'BUY', 'ALL', 'HOA', 'RESEARCH PROSPECTIVE PROPERTY', 'RESEARCH', 3, 'AGENT', 2)
    addDefTask('Leasing Documents, Rents, and Deposits', 'BUY', 'ALL', 'RENTAL', 'RESEARCH PROSPECTIVE PROPERTY', 'RESEARCH', 3, 'AGENT', 2)
    addDefTask('Secure Home Warranty', 'BUY', 'ALL', 'WARRANTY', 'RESEARCH PROSPECTIVE PROPERTY', 'DOCUMENTS', 3, 'BOTH', 2)

    #addDefTaskRollup('PREPARE AND SUBMIT OFFER', True, 'ALL', '', 2)
    addDefTask('Draft Offer', 'BUY', 'ALL', '', 'PREPARE OFFER', 'DOCUMENTS', 3, 'AGENT', 2)
    addDefTask('Review Offer', 'BUY', 'ALL', '', 'PREPARE OFFER', 'MEETING', 3, 'BOTH', 2)
    addDefTask('Contact Sellers Agent', 'BUY', 'ALL', '', 'PREPARE OFFER', 'PHONE/EMAIL', 3, 'AGENT', 1)
    addDefTask('Review Sellers Response', 'BUY', 'ALL', '', 'PREPARE OFFER', 'MEETING',3,  'BOTH', 1)
    addDefTask('Prepare Counter or Decline', 'BUY', 'ALL', 'COUNTER', 'PREPARE OFFER', 'DOCUMENTS',3, 'BOTH', 1)
    addDefTask('Sign Purchase Offer', 'BUY', 'ALL', '', 'PREPARE OFFER', 'DOCUMENTS', 3, 'BOTH', 2)

    #addDefTaskRollup('OFFER ACCEPTED', True, 'ALL', '', 2)
    addDefTask('Deliver Contract to Sellers Agent', 'BUY', 'ALL', '', 'OFFER ACCEPTED', 'EMAIL', 3, 'AGENT', 1)
    addDefTask('Collect Earnest Money', 'BUY', 'ALL', '', 'OFFER ACCEPTED', 'MEETING', 3, 'BOTH', 2)
    addDefTask('Deliver Earnest Money to Sellers Agent', 'BUY', 'ALL', '', 'OFFER ACCEPTED', 'MEETING',3,  'AGENT', 1)

    addDefTask('Track Loan Process', 'BUY', 'ALL', '', 'BUY HOME', 'EMAIL/PHONE', 2, 'AGENT', 2)
    addDefTask('Provide Information to Lender', 'BUY', 'ALL', '', 'BUY HOME', 'EMAIL', 2, 'CLIENT', 2)

    addDefTask('Home Inspection', 'BUY', 'ALL', '', 'BUY HOME', 'MEETING', 2, 'BOTH', 3)
    addDefTask('Septic Inspection', 'BUY', 'ALL', 'SEPTIC', 'BUY HOME', 'EMAIL/PHONE', 2, 'AGENT', 2)
    addDefTask('Well Inspection', 'BUY', 'ALL', 'WELL WATER', 'BUY HOME', 'EMAIL/PHONE',2,  'AGENT', 2)
    addDefTask('Radon Inspection', 'BUY', 'ALL', 'RADON', 'BUY HOME', 'EMAIL/PHONE', 2, 'AGENT', 2)
    addDefTask('Review Appraisal', 'BUY', 'ALL', '', 'BUY HOME', 'MEETING', 2, 'BOTH', 1)

    #addDefTaskRollup('CLOSING', True, 'ALL', '', 2)
    addDefTask('Verify Repairs Complete', 'BUY', 'ALL', '', 'CLOSING', 'EMAIL/PHONE', 3, 'AGENT', 2)
    addDefTask('Order Warranty if Needed', 'BUY', 'ALL', 'WARRANTY', 'CLOSING', 'EMAIL/PHONE', 3, 'AGENT', 1)
    addDefTask('Coordinate Walk Through', 'BUY', 'ALL', '', 'CLOSING', 'EMAIL/PHONE', 3, 'AGENT', 1)
    addDefTask('Coordinate Closing Date and Location', 'BUY', 'ALL', '', 'CLOSING', 'EMAIL/PHONE', 3, 'AGENT', 1)
    addDefTask('Walk Through', 'BUY', 'ALL', '', 'CLOSING', 'MEETING', 3, 'BOTH', 2)
    addDefTask('Buyer Secures Funds', 'BUY', 'ALL', '', 'CLOSING', 'DOCUMENTS', 3, 'CLIENT', 2)
    addDefTask('Closing', 'BUY', 'ALL', '', 'CLOSING', 'MEETING', 3, 'BOTH', 3)

    ## Sell Home Tasks
    #addDefTaskRollup('SELL HOME', False, 'ALL', '', 1)
    addDefTask('Pre-Listing', 'SELL', 'ALL', '', 'PRELISTING', 'MEETING', 2, 'BOTH', '5')
    addDefTask('Property Research', 'SELL', 'ALL', '', 'PROPERTY RESEARCH', 'RESEARCH', 2, 'BOTH', 8)
    addDefTask('Homeowners Association', 'SELL', 'ALL', 'HOA', 'HOMEOWNERS ASSOCIATION', 'RESEARCH', 2, 'BOTH', 2)
    addDefTask('Home Warranty', 'SELL', 'ALL', 'WARRANTY', 'HOME WARRANTY', 'RESEARCH', 2, 'AGENT', 2)
    addDefTask('CMA', 'SELL', 'ALL', '', 'CMA', 'DOCUMENTS', 2, 'AGENT', 1)
    addDefTask('Enter MLS', 'SELL', 'ALL', '', 'MLS', 'DOCUMENTS', 2, 'AGENT', 1)
    addDefTask('Evaluate Upgrades', 'SELL', 'ALL', '', 'UPGRADES', 'RESEARCH', 2, 'BOTH', 2)
    addDefTask('Market the Listing', 'SELL', 'ALL', '', 'MARKETING', 'EMAIL/PHONE', 2, 'AGENT', 2)
    addDefTask('Offer and Contract', 'SELL', 'ALL', '', 'OFFERS', 'DOCUMENTS', 2, 'BOTH', 3)
    addDefTask('Accept Offer', 'SELL', 'ALL', '', 'ACCEPTANCE', 'DOCUMENTS', 2, 'BOTH', 1)
    addDefTask('Track Loan', 'SELL', 'ALL', '', 'FINANCE', 'EMAIL/PHONE', 2, 'AGENT', 2)
    addDefTask('Home Inspections', 'SELL', 'ALL', '', 'INSPECTION', 'MEETING', 2, 'BOTH', 2)
    addDefTask('Appraisal', 'SELL', 'ALL', '', 'APPRAISAL', 'DOCUMENTS', 2, 'AGENT', 1)
    addDefTask('Closing-sell', 'SELL', 'ALL', '', 'CLOSING', 'MEETING', 2, 'BOTH', 2)
    
    
    
    
     

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
    
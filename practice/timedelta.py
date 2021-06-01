#example for working with timedelta objects

#import files needed 
from datetime import date 
from datetime import time 
from datetime import datetime 
from datetime import timedelta

#construct a basic timedelta and print it
print(timedelta(days = 365, hours =5 , minutes =1))

#print todays date 
now = datetime.now()
print("today is: " + str(now))

#print todays date one year from now.
print("one year from now will be: " + str(now + timedelta(days=365)))

#create a timedelta that uses more than one argument. 
print("In 2 days and 3 weeks, it will be: " + str(now + timedelta(days = 2, weeks= 3)))

#create the date 1 week ago, formatted as a string. 
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("one week ago it was: " + s )

#calculate the amount of days it is till the next april fools day. 
today = date.today()
afd = date(today.year, 4, 1)

#use date cpmparison to see if Arpil fools has already gone by for this year
#if it has use the replace() function to get the date for next year. 
if afd < today: 
    print("April fools day already went by %d dats ago" % ((today-afd).days))
    afd = afd.replace(year = today.year+1)

    #now caolculate the amoint of time until april fools day 
time_to_afd = afd-today
print("its just ", time_to_afd.days, "days until april fools day.")
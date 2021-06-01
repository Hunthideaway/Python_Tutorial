#exmple for working with date information
#import the date, time, and datetime classes. 
from datetime import date 
from datetime import time 
from datetime import datetime

def main(): 
    #get otdatys date from teh simple today() ,method from the date class 
    today =date.today()
    print("todays date is", today)

    #print out the dates individual components
    print("date components: ", today.day, today.month, today.year)

    ##retrieve todays week day number 
    print("todays weekday number is: ", today.weekday())
    days = ["mon","tus","wed", "thur", "fri", "sat", "sun"]
    print("which is a: ", days[today.weekday()])

    #get todays date from the datetime class. 
    todays = datetime.now()
    print("the current date and time is: ", todays)

    #get the current time. 
    t = datetime.time(datetime.now())
    print(t)



if __name__ =="__main__":
    main()
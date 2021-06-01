# example for working with os path module. 
#import the data that will be used for the examples
import os 
from os import path 
import datetime 
from datetime import date, time, timedelta
import time 


def main(): 

    #print the name of the os.
    print(os.name)

    #check for item existence and type
    #see if the file exists 
    print("item exist: " + str(path.exists("textfile.txt")))
    #see is something a file 
    print("Item is a file: " + str(path.isfile("textfile.txt"))) 
    # see if something is a directory.
    print("item is a directory: " + str(path.isdir("textfile.txt")))
    #print the path of a file or directory. 
    print("items path: " + str(path.realpath("textfile.txt")))
    #split function to seperate the file name from the path. 
    print("item path and name: " + str(path.split(path.realpath("textfile.txt"))))

    #get the modification time of a file or directory. 
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t) 
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    #calculate how long ago the item was modfied. 
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("it has been " + str(td) + " since the file was modified.")
    print("or, " + str(td.total_seconds()) + " seconds")


if __name__ == "__main__":
    main()
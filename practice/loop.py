#this program shows the user how loops are used within python

def main():
    x=0 

    #while loop 
    while (x<5):
        #print x
        print(x) 
        # increase x by 1 for the next use. 
        x =x+1
    #this is the for loop that is similarly done within c++, for(i=0, i<10, i++)
    for x in range(5, 10):
        print(x)

    #use for loop over a collection
    days =["mon", "tue", "wed", "thur", "frid"]
    for d in days: 
        print(d)

    #use break and continue statements 
    for x in range(5,10): 
        if (x==7): break
        print(x)
    for x in range(1,10): 
        if(x % 2 == 0): continue
        print(x)

    #using the enumerate() function to get index 
    ays =["mon", "tue", "wed", "thur", "frid"]
    for i,d in enumerate(ays):
        print(i, d)

if __name__ == "__main__":
    main()
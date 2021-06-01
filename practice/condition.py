#this program will display how conditions are used within python. 

#main function 
def main():
    x, y = 10, 100

#condtional flow uses if, else if, else
    if (x < y):
        st= "x is less than y"
#this is else if statement
    elif(x == y):
        st = "x is the same as y"
#this is the else statement 
    else:
        st ="x is greater than y"
#print the result htat is found
    print(st)

#condtion statements let you use "a if c else b" which means that all of the above functions are the same as the following single line. 
    st = "x is less than y" if (x<y) else "x is greator than or the same as"
    print(st)

#basic statement that allows for the statement to print as its own program. 
if __name__ =="__main__":
    main()
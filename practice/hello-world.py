#this program is simply used for beginners to see how python is used within the simplest form. 

#this is the main function that has the statements within it.
def main():
    #simple print statement that prints whats in the brackets to the screen. 
    print('Hello World')

    #ask the user to enter their name. 
    name = input('Enter your name: ')

    #the name is stored within the variable name so display it to the user.
    print("nice to meet you, ", name)

#this is used to call main, this helps distiguish when a python code is being included within another program or is the program it  self. 
if __name__ == "__main__":
    main()


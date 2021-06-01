#this prgoram is to show the user for variables work within python. 

#declare a variable 
t=0
#print the variable
print(t)

#redecalre a variable
t ='abc'
#print it back to the screen
print(t)

#this will show the user that the program will not run when using 2 different types. 
print('this is a string ' + str(12))

#global vs local variables in functions 
#this will print of both def and 0 as they are two differnt variables. 
#if you assign a variable to global, as in global = f, this means that f will always be def in our case. 
def function():
    f = "def"
    print(f)

if __name__ == "__main__":
    function()

f = 0
print(f)


#if you want to delete the definition of a variable you use the following.
del f
#then to show that it has changed.
f=3
print(f)


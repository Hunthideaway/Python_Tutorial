#this will show the user how to use functions within python. 

#basic function 
def function1():
    print('this is function1')



#functions that take arguments
def function2(arg1, arg2):
    print(arg1," ", arg2)

#this function returns a calue. 
def cube(x):
    return x*x*x

#function with default value for an argument 
def power(num, x=1):
    result =1
    for i in range(x):
        result = result * num
    return result

#define function with variable numbe rof arguments. 
def multi_arg(*args):
    result =0 
    for x in args: 
        result = result +x 
    return result

    #different ways to call the function 
function1() #prints the statement
print(function1()) #prints the statement then none on the next line since python prints the value of function1 but there is no value for the other set of perenthesis
print(function1) #this displays the location of the function. 
function2(10,20) 
print(function2)
print(power(2))
print(power(2,3)) # this is a loop 
print(multi_arg(2,5,8,3,))
#using class within python

#basic class
class myClass():
    #random data to reference. 
    def method1(self):
        print("m1")

    def method2(self, body):
        print("m2 " + body)

#this is anothe class that shows the user a class inheriting another class 
class another(myClass):

    #random data to reference. 
    def method1(self):
        #call method1 from myClass 
        myClass.method1(self)
        print("another m1")

    def method2(self, body):
        print("another m2 " + body)

#main body.
def main():
    #once you call the class you can call the data in it. 
    c = myClass()
    c.method1()
    c.method2("this is a string")

    c2 = another()
    c2.method1()
    c2.method2("This is string.")
     

if __name__ =="__main__":
    main()
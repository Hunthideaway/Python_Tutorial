#example of how work with files 

def main():

    #open a file for writing and create it if it does not exists. 
    f = open("textfile.txt", "w+")

    #write some lines of data to the file. 
    for i in range(10):
        f.write("this is line " + str(i) + "\r\n")

    #close the file when done. 
    f.close()

    #open the file for appending text to the end. a = append data to the end of the file instead of over writing. 
    f = open("textfile.txt", "a")

    #write some lines of data to the file. 
    for i in range(10):
        f.write("this is line " + str(i) + "\r\n")

    #close the file when done. 
    f.close()

    #open the file to read - r 
    f = open("textfile.txt", "r")

    #make sure that the file has been open in read mode. 
    if f.mode =='r':
        contents = f.read()
        print(contents)

    #read the contents of a file line by line. 
    if f.mode == 'r':
        fl = f.readlines()
        for x in fl: 
            print(x)

if __name__ =="__main__":
    main()
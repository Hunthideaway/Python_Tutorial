#example for retrieving data from the internet 
#to make a request to a web server you must import the following. 
import urllib.request


def main():
    #make a request from a web page. for example purpose google is used. 
    webUrl = urllib.request.urlopen("http://www.google.com")
    print("result code: " + str(webUrl.getcode()))

    #read data and print it out, this prints out the HTML code that creates the google home page. 
    data = webUrl.read() 
    print(data)


if __name__ == "__main__":
    main()
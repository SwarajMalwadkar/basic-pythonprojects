import pyshorteners

url = input("enter the url :")


def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))
    
shortenurl(url)
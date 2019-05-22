import random
import urllib.request

def downloadMyIMG(url):
    name = random.randrange(1,1000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)

downloadMyIMG("http://www.friendzlife.com/wp-content/uploads/2015/02/52639892.jpg")

import urllib2
import urllib

def subscribe(url):
    data = {'email' : 'psu.foodbot@gmail.com', 'fullname' : 'foodbotzen'}

    data = urllib.urlencode(data)

    foo = urllib2.Request(url,data)

    f = urllib2.urlopen(foo)






import urllib2
import urllib

data = {'email' : 'psu.foodbot@gmail.com', 'fullname' : 'foodbotzen'}

url = 'https://www.lists.pdx.edu/lists/subscribe/advocacycluster'
data = urllib.urlencode(data)

foo = urllib2.Request(url,data)

f = urllib2.urlopen(foo)

print f.read()




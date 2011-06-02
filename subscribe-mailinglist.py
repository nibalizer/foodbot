
import urllib2

data = {'email' : 'psu.foodbot@gmail.com', 'fullname' : 'foodbotzen'}

url = 'https://www.lists.pdx.edu/lists/listinfo/advocacycluster'

foo = urllib2.Request(url, data)

urllib2.urlopen(foo)




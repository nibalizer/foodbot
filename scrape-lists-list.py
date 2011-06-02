
import urllib2
import urllib
import BeautifulSoup
from subscribe-mailinglist import subscribe

url = 'https://www.lists.pdx.edu/lists/listinfo'

f = urllib2.urlopen(url)

soup =  BeautifulSoup.BeautifulSoup(f.read())
for i in soup.findAll('a')[2:]:
    url =  i['href']
    print url
    subscribe(url)


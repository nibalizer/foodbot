import urllib2
import urllib

f = open('confirmlist')

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
urllib2.install_opener(opener)

for line in f:
	line = line.replace(' ', '')
	line = line.replace('\n', '')
	tokens = line.split('/')
	code = tokens[6]
	name = tokens[5]

	url = 'https://www.lists.pdx.edu/lists/confirm/' + name + '/' + code
	data = {'realname': 'foodbotzen', 'digests': '0', 'cookie': code, 'language': 'en', 'submit': 'Subscribe to list '+name}
	data = urllib.urlencode(data)
	url = 'https://www.lists.pdx.edu/lists/confirm/' + name
	resp = opener.open(url, data)
	print resp.read()
	resp.close()


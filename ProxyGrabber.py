try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from bs4 import BeautifulSoup
import time
import datetime


sites = ['http://www.proxylists.net/http.txt', 'http://www.proxylists.net/http_highanon.txt',
         'http://multiproxy.org/cgi-bin/search-proxy.pl'
         'http://www.digitalcybersoft.com/ProxyList/fresh-proxy-list.shtml',
         'http://tools.rosinstrument.com/proxy/?rule1',
         'http://www.proxyserverprivacy.com/free-proxy-list.shtml',
         'http://multiproxy.org/txt_all/proxy.txt']


#Input the proxy url
url = "http://www.proxylists.net/http.txt"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)


#Formatting file name
ts = time.time()
dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

file = open("proxylist-" + dt + ".txt", "w")
#Write all text in the file
file.write(text)


#Repeat the whole process with another url
url = "http://multiproxy.org/txt_all/proxy.txt"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

file.write(text)

#Done
file.close()

print("Saved to proxylist-" + dt + ".txt")


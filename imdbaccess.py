#! python3
# imdbaccess.py - Access info about movie from imdb/omdb

import os,sys,bs4,webbrowser,requests
from urllib.parse import urlparse
from os import rename
#print(os.path.exists('.\\Movies'))
#namelist = os.listdir('.\\Movies')
absolute = (os.path.abspath('.\\Movies'))
fname = namelist[0]
copyfname = fname
#API Calls
#res = requests.get('http://google.com/search?q='+' '.join(sys.argv[1:])+' imdb')
res = requests.get('http://google.com/search?q='+ namelist[0] +' imdb')
res.raise_for_status()
searchbs = bs4.BeautifulSoup(res.text,'html.parser')
sLinks = searchbs.select('cite')
firstLink = sLinks[0].get_text() #Use get_text() instead of getText().bs4 syntax
print(firstLink)
#imdblink = firstLink.get('href')
print(len(sLinks))
part = firstLink.rpartition('/')
print(part)
p = part[0]
##id = (part.rpartition('/'))[2]
print(p)
id = p.rpartition('/')[2]
print(id)
data = requests.get('http://www.omdbapi.com/?i='+id+'&plot=short&r=json')
data.raise_for_status()
rating = data.json()['imdbRating']
print(type(rating))
# Renaming part
##for fname in namelist
os.chdir('.\\Movies')
rename(fname,rating+'_'+copyfname)


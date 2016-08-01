#! python3
# lucky.py - Opens several Google search results.
import requests, sys, webbrowser, bs4
print("Googling...")
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
searchbs = bs4.BeautifulSoup(res.text,'html.parser')
linkElems = searchbs.select('.r a')
num = min(3,len(linkElems))
for i in range(num):
    webbrowser.open('http://google.com' + ''.join(linkElems[i].get('href')))        

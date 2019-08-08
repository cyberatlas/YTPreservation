from bs4 import BeautifulSoup
# The built in package for RegEx
import re
from urllib.request import urlopen
# import urllib2

page = urlopen("https://www.youtube.com/user/DEFCONConference/playlists")
html = page.read()
page.close()

soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())
getLinks=soup.findAll('a', href=re.compile('^/playlist\?list='))
# print(getLinks)
for links in getLinks:
    print(links.get('href'))
   youtube-dl -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=<playlistID>

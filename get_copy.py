import os.path

link_download2="http://www.nyaa.se/?page=download&tid=540649"
rss_anime_koi="http://www.nyaa.se/?page=rss&user=176350"
#using feedparser 
import feedparser
import urllib2

#unziped the gziped torrent 
import gzip,urllib2,StringIO


#open rss of dengkun
d = feedparser.parse(rss_anime_koi)


#save path to directory 
save_path="C:/output/"



#for i in range(0,3):
	#getFile=d.entries[i].link
	
	#create file with name str(i) and .torrent 
	#fileName=os.path.join(save_path,str(i)+".torrent")
	
	#write file to above path and save_path
	#file1=open(fileName,"w")
	#write content 
	#file1.write(getFile)
	
	#u = urllib2.urlopen(getFile)
	#fileName.close()
	#localFile = open(str(i)+'.txt', 'w')
	#localFile.write(u.read())
	#localFile.close()
	#torrent file error bencoding
	
	
"""	
for i in range(0,3):
	getFile=d.entries[i].link
	with open(str(i)+'.torrent', "w") as f:
		f.write(urllib2.urlopen(getFile).read())
		f.close()
"""
"""
getFile=d.entries[1].link 
getFile=getFile.replace("#38;","")
with open(str(1)+'.torrent',"w") as f:	
	f.write(urllib2.urlopen(getFile).read())
	f.close()
"""
numOfFiles=10
i=0
while i<numOfFiles: 
	i+=1
	try:
		url=d.entries[i].link
		url=url.replace("#38;","")
		req = urllib2.Request(url)
		opener = urllib2.build_opener()
		response = opener.open(req)
		data = response.read()
		#content-encoding key error => not zipped
		if response.info()['content-encoding'] == 'gzip':
			gzipper = gzip.GzipFile(StringIO(fileobj=data))
			plain = gzipper.read()
			data = plain
		#output.write(data)
		with open(str(1)+'.torrent', "w") as output:
			output.write(data)
			output.close()
	except:
		import webbrowser
		new = 2 # open in a new tab, if possible
		webbrowser.open(url,new=new)
	print "completed download file "+str(i)

"""
from io import BytesIO
torrentURL=d.entries[1].link
correctURL=torrentURL.replace("#38;","")
torrent = urllib2.urlopen(correctURL, timeout=30)
buffer = BytesIO(torrent.read())
gz = gzip.GzipFile(fileobj=buffer)
output = open('1.torrent', 'wb')
output.write(gz.read())
"""


#not a zip file because link is not correct

#remove #38; in link tag to get correct link


#another approach 
#just open url on browser
#browser will download 

#http://pythonconquerstheuniverse.wordpress.com/2010/10/16/how-to-open-a-web-browser-from-python/
"""
torrentURL=d.entries[0].link
correctURL=torrentURL.replace("#38;","")
import webbrowser
new = 2 # open in a new tab, if possible
webbrowser.open(correctURL,new=new)
"""

#count length of items 
#http://stackoverflow.com/questions/6483851/is-there-an-elegant-way-to-count-tag-elements-in-a-xml-file-using-lxml-in-python
#http://stackoverflow.com/questions/13355984/get-errors-when-import-lxml-etree-to-python
"""
from lxml import etree
doc = lxml.etree.parse(rss_dengkun)
count = doc.xpath('count(//item)')
print count
"""




#rss
#channel
#title
#link
#atom:link rel type 
#description

#item 
#title 
#category 
#link
#guid
#description
#pubDate
#/item
#/channel 
#/rss

#with minidom
"""
import xml.dom.minidom
from xml.dom.minidom import Node

dom = xml.dom.minidom.parse("docmap.xml")

def getChildrenByTitle(node):
    for child in node.childNodes:
        if child.localName=='Title':
            yield child

Topic=dom.getElementsByTagName('Topic')
for node in Topic:
    alist=getChildrenByTitle(node)
    for a in alist:
#        Title= a.firstChild.data
        Title= a.childNodes[0].nodeValue
        print Title
"""	
#time
#time.strptime(picturetime, "%I:%M:%S %p")

"""
if os.path.lexists(dest):
    os.remove(dest)
os.symlink(src,dest)
"""

#download
#https://code.google.com/p/metalink-library/
#https://github.com/danfolkes/Magnet2Torrent
#http://dan.folkes.me/2012/04/19/converting-a-magnet-link-into-a-torrent/

#credits:
#http://askubuntu.com/questions/303478/torrents-downloaded-using-python-urllib2-fail-to-open-in-bittorrent-client
import urllib2
import re
from bs4 import BeautifulSoup
import requests
import os
from tqdm import tqdm
import time
headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.116 Chrome/48.0.2564.116 Safari/537.36",
    'dnt': "1",
    'accept-encoding': "gzip, deflate, sdch",
    'accept-language': "en-US,en;q=0.8",
    'cookie': "__cfduid=d503327603003fdad1032fbc161c1a7011457547174",
    'cache-control': "no-cache",
    }
if os.path.isfile('downloads'):
    file=open('downloads','r')
    download=file.read().split('\n')
    file.close()
    count=0
    if os.path.isfile('last'):
        last=open('last','r')
        count=int(last.read())
        last.close()
    else:
        last=open('last','w')
        last.write('0')
        last.close()
    while count<len(download):
        link=download[count]
        filename=link.split('/')[5]
        print 'Downloading',filename
        #dd=requests.request("GET", link, headers=headers,stream=True)
        check=1
        while check!=0:
            time.sleep(3)
            os.system('rm '+filename)
            check=os.system('wget '+link)
        print 'Download Complete, Writing to file'
        '''with open(filename,'wb') as handle:
            for data in tqdm(dd.iter_content()):
                handle.write(data)'''
        count+=1
        last=open('last','w')
        last.write(str(count))
        last.close()
else:
    url='https://www.udacity.com/wiki/ud359/downloads'
    html=urllib2.urlopen(url)
    html=html.read()
    soup=BeautifulSoup(html)
    links=soup.find_all('a',href=re.compile('^http://video.udacity-data.com/zip/ud359/'))
    downloads=[i['href'] for i in links]
    file=open('downloads','w')
    for i in downloads:
        file.write(i+'\n')
    file.close()

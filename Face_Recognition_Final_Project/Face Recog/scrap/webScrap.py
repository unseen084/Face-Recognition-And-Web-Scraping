import urllib.request
import http.cookiejar
import urllib.parse


from urllib.request import build_opener
from urllib.request import urlopen
from urllib.request import HTTPCookieProcessor
from time import sleep
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup
from googletrans import Translator

def imageLookup(imagepath):

    try:
        #imagepath = 'https://ichef.bbci.co.uk/news/660/cpsprodpb/BC3A/production/_92868184_gettyimages-494848232.jpg'
        googlepath = 'http://www.images.google.com/searchbyimage?image_url=' + imagepath
        print(googlepath)
        headers = {}
        headers['User-Agent']= 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        req = urllib.request.Request(googlepath, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        soup = BeautifulSoup(respData, "html.parser")
        
        container = soup.find('div',class_='r5a77d')
        translator = Translator()
        val = translator.translate(container.a.text)
        print(val.text)
        return val.text

    except Exception as e:
        print(str(e))

#imageLookup()
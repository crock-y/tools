#!/bin/python3

import os 
import requests
import datetime

from bs4 import BeautifulSoup

def getImgUrl():
    page=requests.get('http://bing.com');
    html=page.text
    soup = BeautifulSoup(html, "lxml")
    link = soup.head.link;
    return link['href'];

def saveImgs(url,filePath="/home/rock/bingDesktopWallpaper/"):
    fileName = filePath +  str(datetime.datetime.now().date())+'.jpg';
    imgFile=open(fileName, 'wb+');
    req=requests.get(url);
    imgFile.write(req.content);
    return fileName;


if __name__ == "__main__":
    path = getImgUrl();
    url = "http://www.bing.com" + path;
    imagePath = saveImgs(url);
    os.system("gsettings set org.gnome.desktop.background picture-uri file://" + imagePath)

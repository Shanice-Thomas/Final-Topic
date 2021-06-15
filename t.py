import requests
from bs4 import BeautifulSoup
import sys
from matplotlib import pyplot as plt
import json

def day(y,m):
    url = "https://168.motc.gov.tw/countrydeadhurt/%E8%87%BA%E4%B8%AD%E5%B8%82?"+"y="+str(y)+"&m="+str(m)
    return url


def dead(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    result0 = soup.find_all('script')
    data = result0[2].string.split('''"''')
    return data[3]

def hurt(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    result0 = soup.find_all('script')
    data = result0[2].string
    data = data.replace(",","")
    data = data.split('''"''')
    return data[7]

deadlist = []
hurtlist = []

def answer(year):
    for i in range(1,13):
        deadlist.append(int(dead(day(year,i))))
        hurtlist.append(int(hurt(day(year,i))))
        print(str(year)+"年"+str(i)+"月"+"-->"+"死亡人數:"+str(deadlist[i-1])+","+"受傷人數:"+str(hurtlist[i-1]))

answer(105)
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.parse
import re
import time
import math

def get_route_info(deperture, arrival):
    time.sleep(0.5)
    eki1 = urllib.parse.quote(deperture)
    eki2 = urllib.parse.quote(arrival)
    
    url = "https://www.jorudan.co.jp/norikae/cgi/nori.cgi?Csg=1&S=1&pg=0&eki1={eki1}&eki2={eki2}".format(eki1=eki1, eki2=eki2)

    html = request.urlopen(url)

    #set BueatifulSoup
    soup = BeautifulSoup(html, "html.parser")

    keiro = soup.find(id='Bk_list_tbody')
    cost = keiro.find_all('td')[2].string
    transfer = keiro.find(class_='c').string
    price = keiro.find(class_='total').string

    #数字だけ取り出す
    cost = cost.split('時間')
    if len(cost)>1:
        cost = int(re.sub(r'\D', '',cost[0]))*60+int(re.sub(r'\D', '',cost[1]))
    else:
        cost = int(re.sub(r'\D', '', cost[0]))
    
    price = int(re.sub(r'\D', '', price))
    transfer = int(re.sub(r'\D', '', transfer))
    
    #ロジスティックで使う数値を計算
    cal = math.exp((-1)*(-0.163*cost-0.00707*price-transfer))

    return cost, price, transfer, cal
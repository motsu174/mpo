from selenium import webdriver
import time
from . import get_route_info as get
from . import optimizer as opt
from . import person



def optimization(names, nearest_stations,destinations):
    # 人の定義
    N = len(names) #人の数
    persons = []
    for i in range(N):
        p = person.Person(names[i], nearest_stations[i])
        persons.append(p)

    #目的地集合
    destinations = destinations

    #目的地までの情報入力
    for i in range(len(destinations)):
        for j in range(N):
            cost, price, transfer,cal = get.get_route_info(persons[j].near_sta, destinations[i])
            persons[j].set_route(destinations[i], cost, price, transfer,cal)
            persons[j].sum += cal

    #最適値を求める
    return opt.optimizer(persons, destinations)
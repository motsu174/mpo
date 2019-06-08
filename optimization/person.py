import numpy as numpy

class Person:
    def __init__(self, name, nearest_station): #名前と最寄り駅を格納
        self.name = name
        self.near_sta = nearest_station
        self.route = {}
        self.sum = 0

    def set_route(self, destination, cost, price, transfer_num,cal):
        '''
        destination:目的地
        cost:かかる時間
        price:運賃
        transfer_num:乗り換え回数   
        cal:ロジスティックで使う数値
        '''
        self.route[destination] = [cost, price, transfer_num, cal] #目的地までの情報をリストで追加

    def get_route(self, destination):
        return self.route[destination]


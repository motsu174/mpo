import math
from statistics import mean, median,variance,stdev
import numpy as np

def optimizer(persons, destinations):
    destination_opt = '解なし'
    obj = np.inf
    P_vars = {}

    for i in range(len(destinations)):
        Ps = []
        flag=0
        destination = destinations[i]
        
        for j in range(len(persons)):
            if flag ==1:
                continue
            time = persons[j].get_route(destination)[0]
            transfer = persons[j].get_route(destination)[2]
            cal = persons[j].get_route(destination)[3]
            #制約式に当てはまるかどうか
            if time>=120:
                flag=1
            if transfer>3:
                flag=1
            
            #確率計算
            person_u = cal/persons[j].sum
            Ps.append(person_u)

        if flag==1:
            continue
        P_var = variance(Ps)
        
        
        if P_var < obj:
            obj = P_var
            destination_opt = destinations[i]
        
        P_vars[destination] = P_var

    return destination_opt,P_vars
    
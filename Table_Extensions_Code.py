# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:10:02 2022

@author: ameimand
"""

import random
import pandas as pd

num_sim=1000

stocks = _arg1['Symbols']



scenarios=[]
for s in range(0,num_sim):
    l = [random.random() for i in range(0,len(stocks))]
    selected = random.sample(range(0,len(stocks)),k=random.randint(10,15))
    l = [0 if i not in selected else l[i]  for i in range(0,len(stocks))]
    l=[i/sum(l) for i in l]
    scenarios.append(l)

scenarios = pd.DataFrame(scenarios,columns=stocks)

Data = pd.DataFrame()
for i in range(0,len(stocks)):    
    s = scenarios.iloc[:,i].to_list()
    s = pd.DataFrame(s,columns=['Investment'])    
    s = s.reset_index()
    s['Run']=s['index'].apply(lambda x: 'Run'+str(x))    
    s['Symbols_']=stocks[i]
    Data = pd.concat([s,Data])
Data = Data.drop(columns=['index'])
Data = Data.sort_values(by=['Run'])

return Data.to_dict(orient='list')
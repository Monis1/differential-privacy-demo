import numpy as np
import pandas as pd
import random
import seaborn as sns
import matplotlib.pyplot as plt

def read_dataset(dataset):
    data = pd.read_csv(dataset)
    return data

taboo_question = read_dataset("taboo_question.csv")

for i in range(15):
    taboo_question_dp=[]
    for q in taboo_question['Answer']:
        coin_value = random.randint(0,2) # 0 being head, 1 being tails
        if coin_value == 0:
            taboo_question_dp.append(q)
            continue
        coin_value = random.randint(0,2)
        if coin_value == 0:
            taboo_question_dp.append('Yes')
        else:  
            taboo_question_dp.append('No')
       
    taboo_question['Answer'] = taboo_question_dp    
    taboo_question.to_csv(r'dp.csv', index=False)

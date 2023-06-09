import pickle

import pandas as pd
import numpy as np
import pickle
df = pd.read_csv('result_insurance.csv')


#Enter data
age = 34
sex = 1
bmi = 31.2
children = 3 # range(0,5)
smoker = 1
region = 0

if bmi <=27.74:
    bmi1 = 0
elif bmi <= 33.155:
    bmi1 = 1
else:
    bmi1 = 2

if age <=39:
    age1 = 0
else: age1 =1

df = df[df['age']==age1]
#print('age :',df.shape)

df = df[df['sex']==sex]
#print('sex :',df.shape)

df = df[df['bmi']==bmi1]
#print('bmi :',df.shape)

df = df[df['children']==children]
#print('children :',df.shape)

df = df[df['smoker']==smoker]
#print('smoker :',df.shape)

df = df[df['region']==region]
#print('pdays_bin :',df.shape)

pred = df['pred'].item()

print('insurance charges through conditions:',np.round(pred,3))

with open('model_lr.pkl', 'rb') as file:
    loaded_pickle= pickle.load(file)

data = {'age': [age1], 'sex':[sex], 'bmi':[bmi1], 'children':[children], 'smoker':[smoker], 'region':[region]}
new_df = pd.DataFrame(data)
#print(df.to_string())
pred = loaded_pickle.predict(new_df)
print('Insurance charges through pickle:',list(pred)[0])
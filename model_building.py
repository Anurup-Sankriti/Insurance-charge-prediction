import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


#df = pd.read_csv('insurance.csv')
# shape (1338, 7)
# ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
# clockwise region 0,1,2,3
# bmi 0,1,2: 27.74, 33.155, 53.13
#age = 39


df = pd.read_csv('cleaned_insurance.csv')
age_avg = sum(list(df['age']))/len(list(df['age']))
age_low = []
age_high = []
for i in list(df['age']):
    if i <= age_avg:
        age_low.append(i)
    else:
        age_high.append(i)
df.loc[df['age'].isin(age_low), 'age'] = 0
df.loc[df['age'].isin(age_high), 'age'] = 1

#print(df.columns)



model_lr = LinearRegression()
X = df.drop('charges', axis = 1)
Y = df['charges']
model_lr.fit(X, Y)


test_age = list(set(df['age']))
test_sex = list(set(df['sex']))
test_bmi = list(set(df['bmi']))
test_children = list(set(df['children']))
test_smoker = list(set(df['smoker']))
test_region = list(set(df['region']))


test_age_bin = []
test_sex_bin = []
test_bmi_bin = []
test_children_bin = []
test_smoker_bin = []
test_region_bin = []
for i in test_age:
    for j in test_sex:
        for k in test_bmi:
            for l in test_children:
                for m in test_smoker:
                    for n in test_region:
                        test_age_bin.append(i)
                        test_sex_bin.append(j)
                        test_bmi_bin.append(k)
                        test_children_bin.append(l)
                        test_smoker_bin.append(m)
                        test_region_bin.append(n)
test = pd.DataFrame({'age':test_age_bin, 'sex':test_sex_bin, 'bmi':test_bmi_bin, 'children':test_children_bin, 'smoker':test_smoker_bin, 'region': test_region_bin })
print(test.shape)

pred_values = model_lr.predict(test)
test['pred'] = pd.DataFrame(pred_values)

#pickle.dump(model_lr, open('model_lr.pkl', 'wb'))




import  numpy as np
import  pandas as pd

# 코사인유사도
def cos_sim(x, y):
        return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
# user 계산
def fn_sim(user, itemList):
    simList = []
    for i in itemList:
        simList.append(round(cos_sim(user,i),3))
        return  simList
df = pd.read_excel('ITEM_MATRC.xlsx', engine='openpyxl')
print(df.head())
user = [1, 0, 0.33, 0.67, 0.67, 0.67, 0.33, 0, 0.67, 0.33]
itemList = [0]
for i in range(len(df.index)):
    itemList.append(df.loc[i].toList())
print(fn_sim(user,itemList))
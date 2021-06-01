import pandas as pd
df = pd.read_csv('chipotle.csv')
df_tmp=df[['order_id','item_name']]
print(df_tmp.head())
df_tmp_arr=[[]for i in range(1835)]
num=0
for i in df_tmp['item_name']:
    df_tmp_arr[df_tmp['order_id'][num]].append(i)
    num+=1
df_tmp_arr.pop(0)
print(df_tmp_arr)
# pip install mlxtend
# 모든 데이터에 대해서 각 리스트(행마다) 존재하면 True 아니면 False 로 매트릭스 구성
from mlxtend.preprocessing import  TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

te = TransactionEncoder()
te_ary = te.fit(df_tmp_arr).transform(df_tmp_arr)
df = pd.DataFrame(te_ary, columns=te.columns_)
print(df.head())
frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)
asso = association_rules(frequent_itemsets, metric='lift', min_threshold=1)
print(asso)
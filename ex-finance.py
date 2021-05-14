import FinanceDataReader as fdr

import pandas as pd
# pip install -U finance-datareader
# 삼성전자
df2 = fdr.DataReader('005930','2021-01-01', '2021-02-15')
writer = pd.ExcelWriter('005930.xlsx', engine='xlsxwriter')
df2.to_excel(writer, sheet_name='Sheet1')
writer.close()
import matplotlib.pyplot as plt
import mpl_finance
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
mpl_finance.candlestick2_ohlc(ax, df2['Open'], df2['High']
       , df2['Low'], df2['Close'], width=0.5, colorup='r',colordown='b')
plt.show()



# 한국거래소 상장종목 전체 코드
df_krx = fdr.StockListing('KRX')

KOSPI = df_krx[df_krx['Market'].str.contains('KOSPI')]
print(KOSPI)
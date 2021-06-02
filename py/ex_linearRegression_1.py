import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('heights.csv')
x = df['height']
y = df['weight']

line_fitter = LinearRegression()
data = x.values.reshape(-1, 1)
line_fitter.fit(data, y)

print(line_fitter.predict([[70]]))
print(line_fitter.coef_)
print(line_fitter.intercept_)

import matplotlib.pyplot as plt

plt.plot(x, y, 'o')
plt.plot(x, line_fitter.predict(data))
plt.show()
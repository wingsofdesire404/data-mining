import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('elect.xlsx')
x = data['name']
y = data['sales']
plt.figure(figsize = (12, 10))
plt.bar(x, y)
plt.rcParams['font.sans-serif'] = 'Droid Sans Fallback'
plt.xlabel('名称')
plt.ylabel('销售额')
plt.title('销售额柱状图')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
data = read.excel('elec.xlsx')
bins = [0, 170, 340, 510, 680, 850, 1020, 1190, 1360] #分布区间

plt.figure(figsize=(10, 6)) # 图框大小
plt.hist(data['quantity'], 8, range=[0, 1360], alpha=0.8, edgecolor='black')
plt.rcParams['font.sans-serif'] = ['SimHei'] # used to show Chinese character
plt.title('percentage hist of sales', fontsize=20)
plt.xlabel('sales interval')
plt.ylabel('sales number')
plt.xticks(bins)
plt.show()

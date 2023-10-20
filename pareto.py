import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'Droid Sans Fallback'

data = pd.read_excel('elect.xlsx')
x = data['name']
y = data['sales']
y = y.sort_values(ascending=False)
plt.figure(figsize = (12, 10))
plt.bar(x, y)
plt.xlabel('name')
plt.ylabel('sales')
plt.title('pareto graph')

percentage = 1.0 * y.cumsum() / y.sum()
percentage.plot(color='b', secondary_y=True, style='-o', linewidth=2)
plt.show()

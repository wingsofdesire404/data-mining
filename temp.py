import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"simhei.ttf", size=12)  # 使用SimSun字体
plt.text(0.5, 0.5, "你好，世界！", fontproperties=font)
plt.show()


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc("font", family=font)

df_cos = pd.read_csv("./result/files-7_rows-91_선크림.csv", encoding="cp949")
df_all = pd.read_csv("./result/files-7_all.csv", encoding="cp949")

fig, axes = plt.subplots(2, 1, figsize=(10, 17))
plt.subplots_adjust(hspace=0.3)
fig.suptitle("comparison of count & cosine similarity")

sns.barplot(ax=axes[0], data=df_all[:12], x="count", y="name", orient="h")
axes[0].set_title("top 12 count")

sns.barplot(ax=axes[1], data=df_cos[:12], x="cos-score", y="name", orient="h")
axes[1].set_title("top 12 cosine similarity")
plt.show()

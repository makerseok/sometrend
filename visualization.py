import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from matplotlib import font_manager, rc

sns.set()

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc("font", family=font)


def plot_diff(files, rows, keyword):
    print("run visualization.py ...")
    df_cos = pd.read_csv(f"./result/files-{files}_rows-{rows}_{keyword}.csv", encoding="cp949")
    df_all = pd.read_csv(f"./result/files-{files}_all_{keyword}.csv", encoding="cp949")

    fig, axes = plt.subplots(2, 1, figsize=(10, 17))
    plt.subplots_adjust(hspace=0.3)
    fig.suptitle("comparison of count & cosine similarity")

    sns.barplot(ax=axes[0], data=df_all[:12], x="count", y="name", orient="h")
    axes[0].set_title("top 12 count")

    sns.barplot(ax=axes[1], data=df_cos[:12], x="cos-score", y="name", orient="h")
    axes[1].set_title("top 12 cosine similarity")
    plt.savefig(f"./result/figs/files-{files}_{keyword}.png")
    plt.show()


if __name__ == "__main__":
    files = 7
    rows = 91
    keyword = "아모레퍼시픽_선크림"

    df_cos = pd.read_csv(f"./result/files-{files}_rows-{rows}_{keyword}.csv", encoding="cp949")
    df_all = pd.read_csv(f"./result/files-{files}_all_{keyword}.csv", encoding="cp949")

    fig, axes = plt.subplots(2, 1, figsize=(10, 17))
    plt.subplots_adjust(hspace=0.3)
    fig.suptitle("comparison of count & cosine similarity")

    sns.barplot(ax=axes[0], data=df_all[:12], x="count", y="name", orient="h")
    axes[0].set_title("top 12 count")

    sns.barplot(ax=axes[1], data=df_cos[:12], x="cos-score", y="name", orient="h")
    axes[1].set_title("top 12 cosine similarity")
    plt.savefig(f"./result/figs/{keyword}.png")
    plt.show()

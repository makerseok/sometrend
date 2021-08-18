import pickle

import pandas as pd


def concat_data(file):
    with open(file, "rb") as f:
        data_all = pickle.load(f)

    keyword_total = pd.DataFrame()
    data_total = pd.DataFrame()

    for keyword, data in data_all:
        keyword_total = pd.concat([keyword_total, keyword])
        data_total = pd.concat([data_total, data])

    total = pd.concat([keyword_total, data_total], axis=1)
    total.columns = ["name", "count"]

    return total


def run(files, keyword):
    print("run sum_total.py ...")
    filename = f"files-{files}_all_{keyword}"

    total = concat_data(f"./listdata/{filename}")
    total_sum = total.groupby(["name"]).sum()
    total_sum.sort_values(by="count", ascending=False, inplace=True)

    total_sum.to_csv(f"./result/{filename}.csv", index=True, encoding="cp949")
    print(f"./result/{filename}.csv saved")


if __name__ == "__main__":
    files = 7
    keyword = "아모레퍼시픽_선크림"
    filename = f"files-{files}_all_{keyword}"

    total = concat_data(f"./listdata/{filename}")
    total_sum = total.groupby(["name"]).sum()
    total_sum.sort_values(by="count", ascending=False, inplace=True)
    print(total_sum)
    total_sum.to_csv(f"./result/{filename}.csv", index=True, encoding="cp949")
    print(f"{filename}.csv saved")

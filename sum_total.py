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


if __name__ == "__main__":
    filename = "files-7_all"
    total = concat_data(f"./listdata/{filename}")
    total_sum = total.groupby(["name"]).sum()
    total_sum.sort_values(by="count", ascending=False, inplace=True)
    print(total_sum)
    total_sum.to_csv(f"./result/{filename}.csv", index=True, encoding="cp949")
    print(f"{filename}.csv saved")

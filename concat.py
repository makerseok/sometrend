import pandas as pd
import os


def get_excel_files(target_dir, data):
    paths = os.listdir(target_dir)
    for path in paths:
        rawdata = pd.read_excel(os.path.join(target_dir, path), header=14)
        name = rawdata.loc[:, rawdata.columns.str.startswith("연관어")]
        num = rawdata.loc[:, rawdata.columns.str.startswith("건수")]
        data.append([name, num])
    return data


def df_to_list(name, num, lists):
    for i in range(name.shape[1]):
        temp = [[na] * int(nu) for na, nu in zip(name.iloc[:, i], num.iloc[:, i]) if pd.notnull(nu)]
        name_list = sum(temp, [])
        lists.append([name_list])
    return lists


if __name__ == "__main__":
    target_dir = "./rawdata/아모레퍼시픽_선크림"
    data = []
    data = get_excel_files(target_dir, data)
    lists = []
    for name, num in data:
        lists = df_to_list(name, num, lists)
    df = pd.DataFrame(lists)
    print(df)
    for d in df.values:
        print(len(d[0]))

import pandas as pd
import pickle
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
        temp = [
            (na + " ") * int(nu)
            for na, nu in zip(name.iloc[:, i], num.iloc[:, i])
            if pd.notnull(nu)
        ]
        print(temp)
        name_string = " ".join(temp).strip()
        lists.append(name_string)
    return lists


if __name__ == "__main__":
    target_dir = "./rawdata/아모레퍼시픽_선크림"
    data = []
    data = get_excel_files(target_dir, data)
    lists = []
    for name, num in data:
        lists = df_to_list(name, num, lists)
    print(lists)
    for l in lists:
        print(len(l))
    filename = target_dir.split("/")[-1]
    filepath = os.path.join("./listdata", filename)
    with open(filepath, "wb") as f:
        pickle.dump(lists, f)
    print(filepath, "saved")

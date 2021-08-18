import os
from glob import glob
import pickle

import pandas as pd


def get_excel_files(root_dir, data, num_files, target_dir="**", get_all=False):
    files = sorted(glob(f"./{root_dir}/{target_dir}/*.xlsx", recursive=True), reverse=True)

    for i in range(num_files):
        file = files[i]
        rawdata = pd.read_excel(file, header=14)
        name = rawdata.loc[:, rawdata.columns.str.startswith("연관어")]
        num = rawdata.loc[:, rawdata.columns.str.startswith("건수")]
        if get_all:
            data.append([name.iloc[:, -1], num.iloc[:, -1]])
        else:
            data.append([name.iloc[:, :-1], num.iloc[:, :-1]])
    return data


def df_to_list(name, num, lists):
    for i in range(name.shape[1]):
        temp = [[na] * int(nu) for na, nu in zip(name.iloc[:, i], num.iloc[:, i]) if pd.notnull(nu)]
        # temp = []
        # for na, nu in zip(name.iloc[:, i], num.iloc[:, i]):
        #     if pd.notnull(nu):
        #         temp.append([na] * int(nu))
        name_list = sum(temp, [])
        lists.append(name_list)
    return lists


def save_pickle(base_dir, num_files, data, name=None, is_all=False):
    filename = f"files-{num_files}"
    if is_all:
        filename += "_all"
    else:
        filename += f"_rows-{len(data)}"
    filepath = os.path.join(base_dir, filename)
    if name:
        filepath += "_" + name
    with open(filepath, "wb") as f:
        pickle.dump(data, f)
    print(filepath, "saved")


def run(target_dir, num_files):
    print("run concat.py ...")
    root_dir = "./rawdata"
    data = []
    data_all = []
    data = get_excel_files(root_dir, data, num_files, target_dir=target_dir)
    data_all = get_excel_files(root_dir, data_all, num_files, get_all=True, target_dir=target_dir)

    lists = []
    for name, num in data:
        lists = df_to_list(name, num, lists)

    save_pickle("./listdata", num_files, lists, name=target_dir)
    save_pickle("./listdata", num_files, data_all, is_all=True, name=target_dir)
    return num_files, len(lists)


if __name__ == "__main__":
    root_dir = "./rawdata"
    target_dir = "아모레퍼시픽_선크림"
    data = []
    data_all = []
    data = get_excel_files(root_dir, data, target_dir=target_dir)
    data_all = get_excel_files(root_dir, data_all, get_all=True, target_dir=target_dir)

    num_files = len(data)
    print(num_files)

    lists = []
    for name, num in data:
        lists = df_to_list(name, num, lists)
    print(len(lists))
    save_pickle("./listdata", num_files, lists, name=target_dir)
    save_pickle("./listdata", num_files, data_all, is_all=True, name=target_dir)

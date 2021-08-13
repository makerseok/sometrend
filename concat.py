import pandas as pd
import os

# target_dir = "./rawdata/아모레퍼시픽_선크림"
# paths = os.listdir(target_dir)
# for path in paths:
#     rawdata = pd.read_excel(path, header=14)

rawdata = pd.read_excel(
    "./rawdata/아모레퍼시픽_선크림/[썸트렌드] 아모레퍼시픽_연관어 순위 변화_140812-150811.xlsx", header=14
)

name = rawdata.loc[:, rawdata.columns.str.startswith("연관어")]
num = rawdata.loc[:, rawdata.columns.str.startswith("건수")]


def df_to_list(name, num):
    lists = []
    for i in range(name.shape[1]):
        temp = [[na] * int(nu) for na, nu in zip(name.iloc[:, i], num.iloc[:, i]) if pd.notnull(nu)]
        name_list = sum(temp, [])
        lists.append([name_list])
    return lists


lists = df_to_list(name, num)
df = pd.DataFrame(lists)
print(df)

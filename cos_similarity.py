from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def calc_cs(filename, keyword, save=True):
    keyword = keyword.split("_")[-1]
    data = pd.read_csv(f"./tfdf/{filename}.csv", encoding="cp949").transpose()

    target = data.index.get_loc(keyword)
    cs = cosine_similarity(data)

    similar_keyword = list(enumerate(cs[target]))
    sorted_similar_keyword = sorted(similar_keyword, key=lambda x: x[1], reverse=True)
    result = pd.DataFrame(sorted_similar_keyword)
    result.columns = ["key", "cos-score"]

    result["name"] = result["key"].apply(lambda x: data.index[x])
    print(result[:12])
    if save:
        result.to_csv(f"./result/{filename}.csv", index=False, encoding="cp949")
        print(f"./result/{filename}.csv saved")


def run(files, rows, keyword):
    print("run cos_similarity.py ...")
    filename = f"files-{files}_rows-{rows}_{keyword}"
    calc_cs(filename, keyword)


if __name__ == "__main__":
    files = 7
    rows = 91
    keyword = "아모레퍼시픽_선크림"

    filename = f"files-{files}_rows-{rows}_{keyword}"
    calc_cs(filename, keyword)

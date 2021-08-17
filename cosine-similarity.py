from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def calc_cs(filename, keyword, save=True):
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
        result.to_csv(f"./result/{filename}_{keyword}.csv", index=False, encoding="cp949")
        print(f"{filename}_{keyword}.csv saved")


if __name__ == "__main__":
    filename = "files-7_rows-91"
    keyword = "선크림"
    calc_cs(filename, keyword)

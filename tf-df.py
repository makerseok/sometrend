import pickle
import pandas as pd
from tqdm import tqdm


def get_docs_vocab(filename):
    with open(f"./listdata/{filename}", "rb") as f:
        docs = pickle.load(f)

    vocab = list(set(w for doc in docs for w in set(doc)))
    vocab.sort()

    return docs, vocab


def tf(t, d):
    return d.count(t)


def df(t, docs):
    df = 0
    N = len(docs)
    for doc in docs:
        df += t in doc
    return df / N


def tfdf(t, d, docs):
    return tf(t, d) * df(t, docs)


if __name__ == "__main__":
    filename = "files-7_rows-91"
    docs, vocab = get_docs_vocab(filename)

    tfdf_value = [[tfdf(t, d, docs) for t in vocab] for d in tqdm(docs)]
    # tfdf_value = []
    # for d in tqdm(docs):
    #     row = []
    #     for t in vocab:
    #         row.append(tfdf(t, d, docs))
    #     tfdf_value.append(row)
    tfdf_ = pd.DataFrame(tfdf_value, columns=vocab)
    print(tfdf_)
    tfdf_.to_csv(f"./tfdf/{filename}.csv", index=False, encoding="cp949")

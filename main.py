import concat
import tfdf
import cos_similarity
import sum_total
import visualization
import os


def init_folders(dirs):
    for d in dirs:
        if not os.path.exists(d):
            os.mkdir(d)


def run(keyword, num_files):
    files, rows = concat.run(keyword, num_files)

    tfdf.run(files, rows, keyword)
    cos_similarity.run(files, rows, keyword)
    sum_total.run(files, keyword)
    visualization.plot_diff(files, rows, keyword)


if __name__ == "__main__":
    dirs = ["rawdata", "listdata", "tfdf", "result", "result/figs"]
    init_folders(dirs)

    keyword = "아모레퍼시픽_선크림"
    num_files = 1

    run(keyword, num_files)

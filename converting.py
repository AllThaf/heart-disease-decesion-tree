from package.linkedList import LL
from package.functions import *
from package.cleansing import *


def convert():
    # count line
    with open(r"data\heart_2020_cleaned.csv", "r") as file:
        file_len = count_line(file)

    # allocate array of string
    lines = ["" for line in range(file_len)]

    # fill the array
    lines = filling_array(lines)

    # get array
    lines = [split(lines[i]) for i in range(len(lines))]

    # change to float if possible
    lines = [toFloat(lines[i]) for i in range(len(lines))]

    for i in range(18):
        if i in [0, 2, 3, 4, 7, 8, 10, 11, 12, 13, 15, 16, 17]:
            print(i, ll_to_arr(uniquePColumn(lines, i)))


convert()

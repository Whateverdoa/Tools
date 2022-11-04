

import pandas as pd

file_in = r"C:\Users\mike\PycharmProjects\tool_for_vdp\file_in\202057764_1x.csv"

with open(file_in, encoding="utf-8") as f:

    read_lines = f.readlines()
    with open("bewerkt.csv", 'w') as target:

        for lines in read_lines:
            for line in range(1):
                print(lines, end="")



import pandas as pd
import re
import PySimpleGUI as sg
from pathlib import Path
from icecream import ic


def file_to_generator(file_in):
    if Path(file_in).suffix == ".csv":
        file_to_generate_on = pd.read_csv(file_in, ";")

    elif Path(file_in).suffix == ".xlsx":
        ic(Path(file_in).suffix)
        file_to_generate_on = pd.read_excel(file_in,engine='openpyxl')

    elif Path(file_in).suffix == ".xls":
        ic(Path(file_in).suffix)
        file_to_generate_on = pd.read_excel(file_in)

    # file_to_generate_on.replace(['nan', 'None'], '')
    return file_to_generate_on


sg.ChangeLookAndFeel('GreenTan')

import sys

if len(sys.argv) == 1:
    fname = sg.popup_get_file('DE FILE MOET VOLLEDIG ALS TEKST STAAN!!!!')
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:
    # sg.popup('The filename you chose was', fname)
    pad = Path(fname)
    print("volledig pad:")
    print(pad)
    print("naam file met suffix:")
    print(pad.name)
    print("naam file:")
    print(pad.stem)
    print(pad.parent)



    if pad.suffix == ".csv":
        trespa_base = pd.read_csv(fname, ";")
    elif pad.suffix == ".xlsx":
        trespa_base = file_to_generator(pad).replace(['nan', 'NaN', 'None', "."], '')

    # print(trespa_base.aantal.sum())

        df1 = trespa_base
        a = df1['Colorcode']
        b = df1['num']

        regex = r"([. -])"
        subst = ""

        links = []
        # try except inbouwen voor als eerste regel een integer bevat!!!!
        for line in a:
            line = str(line)
            print(line)
            a = "".join(line.strip("\n"))
            result = re.sub(regex, subst, a, 0, re.MULTILINE)
            links.append(f'{result}-')

        rechts = [str(line) for line in b]

        # code = [i + j for i, j in zip(links, rechts)]

        code_word = pd.DataFrame([i + j for i, j in zip(links, rechts)])

        print(code_word.head(2))

        df1['code'] = code_word

        zonder_csv = fname.split(".csv")
        a = ''.join(zonder_csv)

        print(f'zonder csv:{pad.stem}')
        df1.to_csv(f'{pad.parent / pad.stem}_metcode.csv', ";", index=0)
        df1.to_excel(f'{pad.parent / pad.stem}_metcode.xlsx', index=0)

        print(df1.head(1))
        print(df1.tail(1))



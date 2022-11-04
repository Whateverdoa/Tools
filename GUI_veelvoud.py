import pandas as pd
import PySimpleGUI as sg
from pathlib import Path

from icecream import ic
from openpyxl import load_workbook
import xlrd
import xlwt


sg.ChangeLookAndFeel('Black')

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

import sys

if len(sys.argv) == 1:
    fname = sg.popup_get_file('csv of xls file: '
                              'De kolom met header "veelvoud" is de aantal per regel')
else:
    fname = sys.argv[1]
    print(fname)


if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:
    # sg.popup('The filename you chose was', fname)
    pad = Path(fname)
    print("volledig pad:")
    ic(pad.parent)
    print("naam file met suffix:")
    print(pad.name)
    print("naam file:")
    ic(pad.stem)
    ic(pad.parent)

    generator = file_to_generator(pad).itertuples(index=True)
    nieuwe_df = []

    for rows in generator:

        for i in range(int(rows.veelvoud)):
            # todo if else logic on rolnummer to build wikkel etc..
            nieuwe_df.append(rows)

    verwerkte_file_in = pd.DataFrame(nieuwe_df, dtype="string")

    ic(verwerkte_file_in.head())
    ic(verwerkte_file_in.shape)

    paduit = f'{Path(pad.stem)}_argv__{pad.suffix}'
    ic(paduit)
    ic(pad.suffix)
    ic(pad.joinpath(paduit))

    if pad.suffix == ".csv":

        verwerkte_file_in.to_csv(pad.parent.joinpath(paduit), index=0)
    elif  pad.suffix == ".xls" or ".xlsx":
        verwerkte_file_in.to_excel(pad.parent.joinpath(paduit), index=False)
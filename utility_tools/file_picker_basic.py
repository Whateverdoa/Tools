import pandas as pd

import re
import PySimpleGUI as sg
from pathlib import Path

sg.ChangeLookAndFeel('Reddit')

import sys

if len(sys.argv) == 1:
    fname = sg.popup_get_file('Document to open, click ok to continue!!')
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

    df = pd.read_csv(fname, ";")
    print(df.head())

    print(df.aantal.sum())




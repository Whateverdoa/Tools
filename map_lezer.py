#!/usr/bin/python3

from datetime import date, timedelta
from pathlib import Path
import pandas as pd

import re
import PySimpleGUI as sg

import sys

def find_ordernummers_in(folder):
    past_time = date.today() - timedelta(minutes=1)
    filesinmap=[]
    for path in Path(folder).iterdir():
        timestamp = date.fromtimestamp(path.stat().st_mtime)

        # if path.is_file() and past_time > timestamp:
        #     print(f'files: {path}')
        #     filesinmap.append(path)
        if path.is_dir():
            print(f"{path.name =}")
            filesinmap.append(path.name)
            print(path.is_dir())
    map_met_int = [int(x) for x in filesinmap]
    return  map_met_int


def hoogste_ordernummer(lijst_van_te_controleren_mappen):
    hoogste_ordernummer = max(set(lijst_van_te_controleren_mappen))
    hoogste_ordernummer_plus_1 = int(hoogste_ordernummer) + 1
    print(hoogste_ordernummer_plus_1)
    return hoogste_ordernummer_plus_1

#standaard_python functie max hernoemd
max_ordernummer = hoogste_ordernummer



def standaard_map(begin_nummer, max_ordernummer):

    eind = int(max_ordernummer)
    map_lijst = [x for x in range(int(begin_nummer), eind)]
    return map_lijst


def mappen_vergelijker(standaardmap, opgehaalde_map):
    niet_aanwezig = list(set(standaardmap) - set(opgehaalde_map))
    if niet_aanwezig == []:
        return 0
    return niet_aanwezig

sg.ChangeLookAndFeel('Reddit')



if len(sys.argv) == 1:
    fname = sg.popup_get_folder('Document to open, click ok to continue!!')
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no folder supplied")
else:
    # sg.popup('The filename you chose was', fname)
    pad = Path(fname)
    print("volledig pad:")
    print(pad)
    print("naam file met suffix:")
    print(pad.name)
    print("naam file:")
    print(pad.stem[4])
    print(pad.parent)


    te_checkenlijst = find_ordernummers_in(pad)
    print(te_checkenlijst)
    standaard_map = standaard_map(202224000, max_ordernummer(te_checkenlijst))

    niet_aanwezig=sorted(mappen_vergelijker(standaard_map,te_checkenlijst))


    # df = pd.read_csv(fname, ";")
    # print(df.head())
    #
    # print(df.aantal.sum())


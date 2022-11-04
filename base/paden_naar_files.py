# import pandas as pd
from pathlib import Path

from datetime import date, timedelta
from icecream import ic

file_in_map = r"file_in/te_gebruiken"
wdir = Path.cwd()
file_in = wdir / file_in_map
folder_file_in = wdir / file_in_map


ic(wdir)
ic(file_in.is_file())

file_out = wdir / "file_out/"
file_out2 = wdir / "file_out/rolaantallen.csv"
# file_tmp = wdir / "file_out/tmp"
# file_tmp_2 = wdir / "file_out/tmp2"



#
# print(vert.is_dir())
file_concat = Path(r"C:\Users\mike\PycharmProjects\Projekt_lijstbewerken\source\file_out\concat")

# file_tmp_2.mkdir(parents=True, exist_ok=True)
# file_tmp.mkdir(parents=True, exist_ok=True)


def cleaner(pad):

    dir_to_empty = sorted(Path(pad).glob('*.csv'))

    for file in dir_to_empty:
        file.unlink()


def remove_files(folder):
    past_time = date.today() - timedelta(days=21)

    for path in Path(folder).iterdir():
        timestamp = date.fromtimestamp(path.stat().st_mtime)
        if path.is_file() and past_time > timestamp:
            print(f'deze files worden gedelete!: {path}')
            path.unlink() # Delete files
        if path.is_dir():
            print(path.is_dir())
            #remove_files(path)
        else:
            # print(f'{path} blijft bestaan')
            pass
        try:
            pass
        except (FileNotFoundError, WindowsError):
            pass

pad_data_laserstans = Path("//fileserver/data/laserstans")
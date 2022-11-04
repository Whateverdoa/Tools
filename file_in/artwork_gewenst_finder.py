from pathlib import Path
import datetime
import os


# path = r"E:\demos\files_demos\sample.txt"
pad_naar_pdf = Path(r"M:\ESKO\Products\E\ETIKET NEDERLAND BV\21015000-21015999\460521015658\460521015658.pdf")

# file modification timestamp of a file
m_time = os.path.getmtime(pad_naar_pdf)
# convert timestamp into DateTime object
dt_m = datetime.datetime.fromtimestamp(m_time)
print('Modified on:', dt_m)

# file creation timestamp in float
c_time = os.path.getctime(pad_naar_pdf)
# convert creation timestamp into DateTime object
dt_c = datetime.datetime.fromtimestamp(c_time)
print('Created on:', dt_c)


def find_modtime_(pad_naar_file):
    """return modification time of a file"""
    result = Path(pad_naar_file).stat().st_mtime
    return result

mod_to_find = 1565766235.4697597

if find_modtime_(pad_naar_pdf)==mod_to_find:
    print(f'{pad_naar_pdf.stem} is een artwork gewenst file')
else:
    print('not found')
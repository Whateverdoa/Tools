from typing import List

import pandas as pd
from pathlib import Path
import base.paden_naar_files as paden
import base.calculations as function

filecsv = r"file_in/te_gebruiken/"
print(paden.file_in)


folder_file_in_lijst = [rol for rol in paden.folder_file_in.glob("*.csv") if rol.is_file()]
aantal_files= len(folder_file_in_lijst)



print(folder_file_in_lijst)

naam_shirt = "202259734 sets van 150 "
serie_van = 153
namen_uit_lijst = function.file_name_maker_met_pad(aantal_files, paden.file_out, naam_shirt)

count=0
for file in folder_file_in_lijst:

    function.repeater_van_files(file, namen_uit_lijst[count], serie_van)
    count += 1




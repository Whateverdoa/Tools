from pathlib import Path
import pandas as pd
from icecream import ic


def repeater_van_files(file_in_naam, file_naam_uit, repeteer=1):
    """"with filein """
    with open(file_in_naam, "r", encoding="utf-8") as readf:
        readline = readf.readlines()

    with open(file_naam_uit, "w", encoding="utf-8") as fwrite:
        fwrite.writelines(readline[0:1])
        for i in range(repeteer):
            fwrite.writelines(readline[1:])
            fwrite.writelines("\n")


def file_name_maker_met_pad(
        amount_of_rolls, posix_destination_pad, filename: "str", exp=".csv"
):
    """a list comprehension to supply names for csv files
    give a start naam and it will generate a list  of names for the amount of rolls """
    man_fac_name_with_path_list = []
    for naam in range(amount_of_rolls):
        manufactored_name_with_path = (
            f"{Path(posix_destination_pad / filename)}_{naam + 1:>{0}{5}}{exp}"
        )
        # print(manufactored_name_with_path)
        man_fac_name_with_path_list.append(manufactored_name_with_path)

    return man_fac_name_with_path_list


def file_to_generator(file_in):
    if Path(file_in).suffix == ".csv":
        file_to_generate_on = pd.read_csv(file_in, ";")

    elif Path(file_in).suffix == ".xlsx":
        ic(Path(file_in).suffix)
        file_to_generate_on = pd.read_excel(file_in, engine='openpyxl')

    elif Path(file_in).suffix == ".xls":
        ic(Path(file_in).suffix)
        file_to_generate_on = pd.read_excel(file_in)

    # file_to_generate_on.replace(['nan', 'None'], '')
    return file_to_generate_on


def nummer_oplopend(nummer, aantal):
    eind = nummer + aantal
    num = [f'{x:>{0}{4}}' for x in range(nummer,eind)]
    # print(pd.DataFrame([num]).head(5))
    return pd.DataFrame([num], columns=["num"])

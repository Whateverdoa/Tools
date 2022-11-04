from pathlib import Path
import shutil
import pandas as pd

pad = Path(r"E:\testgrond\E\ENGELVAART BODYWEAR B.V")

padcwd = Path.cwd().parent
input_pad = Path(r"E:\testgrond\E\ENGELVAART BODYWEAR B.V\21001000-21001999\168221001239\VDP\items")
print(input_pad)
paduit = pad.joinpath("21001000-21001999")


inte_lezen_map_met_pdfs = sorted(Path(input_pad).rglob("*.pdf"))

destination = r"E:\testgrond\E\ENGELVAART BODYWEAR B.V\output_pdfs"
output_pdf_map = Path(destination)

output_pdf_map.mkdir(parents=True, exist_ok=True)



def copy_file_to(source, destination_folder):


    try:
        shutil.copy(source, destination_folder)
        print(f"File {source.stem} copied successfully to {destination_folder}.")

    # If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.")

    # If there is any permission issue
    except PermissionError:
        print("Permission denied.")

    # For other errors
    except:
        print(f"Error occurred while copying file {source.stem}.")


for file_output_name in inte_lezen_map_met_pdfs:
    pad_file_naam = Path(f'{paduit}/{file_output_name.stem}/{file_output_name.name}')
    copy_file_to(output_pdf_map,pad_file_naam)
    print(pad_file_naam)


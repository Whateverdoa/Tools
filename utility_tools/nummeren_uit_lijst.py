import pandas as pd
import PySimpleGUI as sg
from pathlib import Path
import calculations.calculations as function
from icecream import ic
from openpyxl import load_workbook
import xlrd
import xlwt


sg.ChangeLookAndFeel('Black')

import sys

if len(sys.argv) == 1:
    fname = sg.popup_get_file('csv of xls file: '
                              'De kolom met header "aantal" is de aantal per regel')
else:
    fname = sys.argv[1]

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

    # bewerk eerst nieuwe_df
    dfdf = file_to_generator(pad).replace(['nan', 'NaN', 'None',"."], '')
    ic(dfdf.tail())

    # generator = function.file_to_generator(pad).itertuples(index=True)
    generator = dfdf.itertuples(index=True)
    nieuwe_df = []

    def groen_wit_wissel(x):
        if int(x) > 3:
            return "geenpijl.pdf"
        else:
            return "pijl.pdf"




    for rows in generator:


        # todo if else logic on rolnummer to build wikkel etc..
        # todo als prefix = nan vervangewn door leeg veld


        begin = int(rows.begin)
        eind = int(rows.begin + rows.aantal)
        print(begin)
        print(rows)

        # num	vv	begin	prefix	aantal	pdf	eind
        # a = pd.DataFrame([(f'{rows.prefix}{x:>{0}{4}}', " ",  f'{rows.pdf}') for x in range(begin , eind) for i in range(rows.veelvoud)], columns=["Kolom", "omschrijving","pdf"])

        # begin,aantal,beeld
        # a = pd.DataFrame([(f'{x:>{0}{3}}', " ",  f'{rows.pdf}') for x in range(begin,eind)], columns=["Kolom", "omschrijving","pdf"])


        # a = pd.DataFrame([(f'{x:>{0}{rows.posities}}', " ",  f'{rows.pdf}') for x in range(begin,eind)], columns=["Kolom", "omschrijving","pdf"])


        # RISA BV
        # a = pd.DataFrame([(f'{rows.prefix}{x:>{0}{1}}', " ",  f'{rows.pdf}',  f'{rows.beeld}') for x in range(begin,eind)], columns=["Kolom", "omschrijving","pdf","achtergrond"])

        # servopack 202235726
        # a = pd.DataFrame([(f'{rows.prefix}{x:>{0}{5}}', " ",  f'{rows.pdf}') for x in range(begin , eind) for i in range(rows.veelvoud)], columns=["Kolom", "omschrijving","pdf"])

        # a = pd.DataFrame([(f'{rows.prefix}{x:>{0}{rows.posities}}', " ",  f'{rows.pdf}') for x in range(begin,eind)], columns=["Kolom", "omschrijving","pdf"])

        #hazenberg hoefsloot
        # a = pd.DataFrame([(f'{rows.prefix}{x:>{0}{rows.posities}}', " ",  f'{rows.pdf}', f'{rows.beeld}')
        #                   for x in range(begin,eind)], columns=["Kolom", "omschrijving","pdf","beeld"])

        # etiket nederland 202227951
        # a = pd.DataFrame([(f'{x:>{0}{rows.posities}}', " ",  f'{rows.pdf}', f'{rows.beeld}') for x in range(begin,eind)], columns=["Kolom", "omschrijving","pdf","beeld"])

        #deko
        # a = pd.DataFrame([(f'{x:>{0}}{rows.postfix}', " ",  f'{rows.pdf}', f'{rows.beeld}') for x in range(begin,eind)], columns=["Kolom", "omschrijving","pdf","beeld"])


        # a = pd.DataFrame([(f'{rows.begin}{rows.prefix}{x:>{0}{2}}', " ",  f'{rows.pdf}') for x in range(1 , 11)], columns=["Kolom", "omschrijving","pdf"])

        # begin	eind	prefix	volt	pdf	aantal	bnum	enum
        # a = pd.DataFrame([(f'{rows.prefix}{x:>{0}{5}}', " ",  f'{rows.pdf}', f'{rows.volt}') for x in range(begin , eind)], columns=["Kolom", "omschrijving","pdf", "Volt"])

        #servopack  datum	kleur	veelvoud	prefix	aantal	begin	eind
        a = pd.DataFrame([(f'{rows.prefix}{x:>{0}{3}}', " ", "leeg.pdf",  f'{rows.kleur}',f"{rows.datum}" ) for x in range(begin , eind)], columns=["Kolom", "omschrijving","pdf", "kleur","datum"])


        # a = pd.DataFrame([(f'{rows.prefix}{x:>{0}{4}}', " ",  f'{rows.pdf}', f'{rows.produkt}') for x in range(begin , eind)], columns=["Kolom", "omschrijving","pdf","produkt"])

        # a = pd.DataFrame([(f'{x:>{0}{1}}{rows.postfix}', " ",  f'{rows.pdf}') for x in range(begin , eind)], columns=["Kolom", "omschrijving","pdf"])

        #APLUS
        # a = pd.DataFrame([(f'{rows.prefix}{x:>{0}{3}}', f'{rows.kleur}', " ",  f'{rows.pdf}') for x in range(begin , eind) for i in range(rows.veelvoud)], columns=["Kolom", "kleur","omschrijving","pdf"])

        # etikettenkoning


        # a = pd.DataFrame([(f'{rows.prefix}{x:>{0}{3}}', f'{rows.kleur}', " ",  f'{rows.pdf}') for x in range(begin , eind)], columns=["Kolom", "kleur","omschrijving","pdf"])


        # a = pd.DataFrame([(f'{rows.prefix}{x:>{0}{4}}', f'{rows.kleur}', " ",  f'{rows.pdf}') for x in range(begin , eind)], columns=["Kolom", "kleur","omschrijving","pdf"]) # groen
        # a = pd.DataFrame([(f'{x:>{0}{4}}', f'{rows.kleur}', " ",  f'{rows.pdf}') for x in range(begin , eind)], columns=["Kolom", "kleur","omschrijving","pdf"]) # wit


        # a = pd.DataFrame([(f'{x:>{0}{4}}', " ",  f'{rows.pdf}') for x in range(begin , eind) ], columns=["Kolom","omschrijving","pdf"]) #wit

        # a = pd.DataFrame([(f'{x:>{0}{8}}', " ",  f'{rows.pdf}',f'{rows.maand}') for x in range(begin , eind) ], columns=["Kolom","omschrijving","pdf","maand"])
        # a = pd.DataFrame([(f'{x:>{0}{1}} {rows.postfix}', " ",  f'{rows.pdf}') for x in range(begin , eind) ], columns=["Kolom","omschrijving","pdf"])

        # a = pd.DataFrame([(f'{rows.prefix}{x:>{0}{2}}', " ", f'{rows.pdf}', groen_wit_wissel(x)) for x in range(begin , eind) for i in range(1)], columns=["kolom","omschrijving","pdf","kleur"])

        # nummers =function.nummer_oplopend(rows.begin, rows.aantal)
        # nieuwe_df.append(nummers)

        # b= lege velden dan concat a+b

        ic(a.head())
        nieuwe_df.append(a)


    verwerkte_file_in = pd.concat(nieuwe_df)
    #custom stukje_

    # verwerkte_file_in['slice4links']= verwerkte_file_in["Kolom"].apply(lambda x: x[:4])
    # verwerkte_file_in['slice4rechts']= verwerkte_file_in["Kolom"].apply(lambda x: x[-4:])
    # verwerkte_file_in['met_punt']= verwerkte_file_in["Kolom"].apply(lambda x: str(x.replace(",",".")))



    ic(verwerkte_file_in.head())
    ic(verwerkte_file_in.shape)

    paduita = f'{(pad.stem)}_nieuwe_lijst{pad.suffix}'
    ic(pad.stem)
    ic(paduita)
    ic(pad.suffix)
    ic(pad.joinpath(paduita))

    if pad.suffix == ".csv":
        verwerkte_file_in.to_csv(pad.parent.joinpath(paduita), index=0)
    elif pad.suffix == ".xls" or ".xlsx":
        ic(pad.parent)
        verwerkte_file_in.to_excel(pad.parent.joinpath(paduita), index=0)

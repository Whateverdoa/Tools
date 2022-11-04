import math
import pandas as pd
from openpyxl import load_workbook
import xlrd
import xlwt
from icecream import ic
from pathlib import Path

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


def wikkel(Aantalperrol, formaat_hoogte, kern=76):
    """ importing in a function?
    er word altijd plus 2 toegevoegd aan etiketten"""
    pi = math.pi
    # kern = 76  # global andere is 40
    materiaal = 145  # global var
    var_1 = math.ceil(math.sqrt((4 / pi) * ((Aantalperrol * formaat_hoogte) / 1000) * materiaal + pow(kern, 2)))
    wikkel = int(2 * pi * (var_1 / 2) / formaat_hoogte + 2)
    return wikkel


def buiten_diameter():
    """in millimeters"""
    pi = math.pi
    materiaal = 145
    def bdmtr(Aantalperrol, formaat_hoogte, kern=76):
        var_1 = math.ceil(math.sqrt((4 / pi) * ((Aantalperrol * formaat_hoogte) / 1000) * materiaal + pow(kern, 2)))
        return var_1
    return bdmtr


def sheet(xwaarde=1,ywaarde=1):
    sheet = xwaarde*ywaarde
    return sheet

def aantalsheets(totaal,sheet=1):
    """aantal sheets geeft een (int) naar boven afgerond positief getal"""
    tot_sheets = math.ceil(totaal/sheet)

    return tot_sheets

def doortrek(ywaarde, hoogte, tussenruimte):
    doortrek = (hoogte+tussenruimte)  * ywaarde
    return doortrek



def sheets_to_meters(tot_sheets, doortrek):
    meters = (tot_sheets * doortrek)/1000
    return meters



def inloop_uitloop_sheets(doortrek):
    in_uit_waarde = 20 * doortrek / 1000

    return in_uit_waarde


def vdp_lengte(sheets_meters, in_uit_):
    totale_vdplengte = math.ceil(sheets_meters + in_uit_)
    return totale_vdplengte

def beg_nummers():
    def begin_nummer(begin_nummer, totaal, apr):

        begin_nummers=[ x for x in range(begin_nummer,totaal-1,apr)]
        return begin_nummers
    return begin_nummer


# aantal = 32000
# aantal_per_rol = 2000
# ######
# tussenruimte_y = 3
# mes_hoogte = 35 + tussenruimte_y  ######
# Etiketten_y = 25  #####
# aantal_sheets = (aantal // Etiketten_y)
# banen = 5
# aantal_sheets_p = ((aantal // Etiketten_y) // banen) + 20


# def rol_in_order():
#
#
#     return math.ceil((aantal_per_rol / Etiketten_y))  # ceil is afgerond naar dichtbijzijnste integer
#
#
# print(
#     f'de eerste wikkel staat na {rol_in_order() + 10} sheets, de volgende wikkel staat na elke {rol_in_order()} sheets')
# print(f'aantal sheets = {aantal_sheets_p}')
# spronglijst = list(range((rol_in_order() + 10), aantal_sheets // banen, rol_in_order()))
# print(spronglijst)
# len(spronglijst)


def sheets_per_rol_per_baan(aantal, etiket_y, etiket_x):
    sheets_per_baan=math.ceil((aantal / etiket_y) / etiket_x)
    return int(sheets_per_baan)

########
# aantal = 100000
# aantal_per_rol = 2500
# ######
# tussenruimte_y = 3
# mes_hoogte = 12 + tussenruimte_y  ######
# Etiketten_y = 65  #####
# aantal_sheets = (aantal // Etiketten_y)
# banen = 4
# aantal_sheets_p = ((aantal // Etiketten_y) // banen) + 20


def rol_in_order(aantal_per_rol, Etiketten_y, aantal_sheets, banen):

    rol_in_order = math.ceil((aantal_per_rol / Etiketten_y))
    spronglijst = list(range((rol_in_order + 10), aantal_sheets // banen, rol_in_order))


    return  spronglijst


# print(
#     f'de eerste wikkel staat na {rol_in_order() + 10} sheets, de volgende wikkel staat na elke {rol_in_order()} sheets')
# print(f'aantal sheets = {aantal_sheets_p}')
# spronglijst = list(range((rol_in_order() + 10), aantal_sheets // banen, rol_in_order()))
# print("#" * 20)
# print(spronglijst)
# print("#" * 20)
# print(f'aantal combinaties met wikkel in vdp = {len(spronglijst)}')
# print("#" * 20)





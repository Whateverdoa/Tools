from .berekeningen import *

breedte = 35.0
hoogte = 100.0
xwaarde = 8
ywaarde = 9
tussenruimte = 3.00
totaal = 75000
apr = 1000
kern = 76


def test_sheet():
    test = sheet(xwaarde, ywaarde)
    assert test == 72


def test_aantalsheets():
    test = aantalsheets(totaal, sheet(xwaarde, ywaarde))
    assert test == 1042


def test_doortrek():
    test = doortrek(ywaarde, hoogte, tussenruimte)
    assert test == 927


def test_wikkel():
    test = wikkel(apr, hoogte, kern)
    assert test == 6


def test_buiten_diameter():
    roldiameter = buiten_diameter()
    test = roldiameter(apr, hoogte, kern)
    assert test == 156


def test_inloop():
    test = inloop_uitloop_sheets(doortrek(ywaarde, hoogte, tussenruimte))
    assert test == 18.54


def test_sheets_to_meters():
    test = sheets_to_meters(aantalsheets(totaal, sheet(xwaarde, ywaarde)), doortrek(ywaarde, hoogte, tussenruimte))

    assert test == 965.934


def test_vdp_lengte():
    test = vdp_lengte(965.934, 18.54)
    assert test == 985


def test_beg_nummers():
    testing = beg_nummers()
    tist = testing(1,totaal,apr)
    assert tist == []


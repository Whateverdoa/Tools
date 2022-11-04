# /usr/bin/env python3

import pandas as pd
'''Functie om de checkdigit te leveren bij een mod 43 en een mod 43 reversed
dit werkt nu nog even netjes functie maken in FP
'''

keys= [*range(43)]
returnvalues= "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-. $/+%"

checkdigits= [x for x in returnvalues]
checkdigits_reversed = [x for x in reversed(checkdigits)]

checkdigit_norm_dikt = dict(zip(keys, checkdigits))
check_digit_rev_dict = dict(zip(keys, checkdigits_reversed))


def check_if_int(num):
    try:
        num = int(num)
    except ValueError:
        return False

    return True


def make_referencenumber(hexstringin):
    
   # input lijst maken string dan string opdelen in getallen en characters
   revnum = sum([int(num) for num in hexstringin if num.isdigit()])
   # print(revnum)
   # revcharacters = [num for num in hexstringin if ord(num) == True]
   string_to_list = sum(ord(x)-55 for x in hexstringin if check_if_int(x) == False)
   

   return revnum + string_to_list


def referencenumber(reverence_num):
    rev_num = reverence_num % 43

    return rev_num


def checkdigit(dikt, rev_number):
    key= int(rev_number)
    cd = dikt[key]
    return cd


#
# for key, value in check_digit_rev_dict.items():
#     print(key, value)

print(referencenumber(make_referencenumber('159AZ')))

print(checkdigit(check_digit_rev_dict, referencenumber(make_referencenumber('75C858'))))
print(checkdigit(checkdigit_norm_dikt, referencenumber(make_referencenumber('159AZ'))))



totaal_aantal_order = 50_000

# vul laatste nummer vorige keer in PLUS 1
begin_hex_string = "75C858"

begin = int(begin_hex_string , base=16)
eind = begin + totaal_aantal_order

dec_reeks=[hex(x)[-6:].upper() for x in range(begin, eind)]
met_mod43_rev = [(f'{code}',f'**00{code}{checkdigit(check_digit_rev_dict, referencenumber(make_referencenumber(code)))}**','','leeg.pdf') for code in dec_reeks]

df_met_mod43 = pd.DataFrame(met_mod43_rev, columns=['kolom1','code','omschrijving','pdf']).astype(str)

df_mod43_csv = df_met_mod43.to_csv('202252560.csv')
df_mod43_csv_excel = df_met_mod43.to_excel('202252560.xlsx')
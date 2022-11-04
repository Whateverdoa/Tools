from mod10 import *

def test_mod_codabar():
    # Digits: A
    # 7
    # 8
    # 9
    # A
    # Reference
    # numbers: 16
    # 7
    # 8
    # 9
    # 16
    # Sum
    # of
    # reference
    # numbers: 56
    # Calculate
    # checksum: 56 / 16 = 3
    # Remainder
    # 8
    # difference: 16 - 8 = 8
    # Check
    # digit
    # Reference
    # number
    # 8 = 8
    test = mod_codabar(74000812700)
    print(test)

    assert test == 1

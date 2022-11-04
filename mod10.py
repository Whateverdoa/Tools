

def luhn_checksum(number):

  digits = list(map(int,str(number)))
  reversedDigits = digits[::-1]
  total = 0
  for position, digit in enumerate(reversedDigits):
    if (position + 1) % 2 == 1:
       digit *= 2
       if digit > 9:
        digit -= 9
    total += digit
    total = total * 9

    return str(total % 10)

# Result.Value=luhn_checksum(BaseNumber.Value)
# 35050

print(luhn_checksum(201041000))

def mod_codabar(number):
    digits = list(map(int, str(number)))
    A = 16
    D = 19
    digits = (sum(digits))+(A+D)
    print(digits)
    cd = digits % digits//16
    return cd


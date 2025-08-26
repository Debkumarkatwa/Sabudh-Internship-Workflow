def int_to_roman(num: int) -> str:
    data = {1000:'M',
         500:'D', 
         100:'C', 
         50:'L', 
         10:'X',
         5:'V',
         1:'I'
        }   # dictionary to store the roman values
    
    roman = ''  # to store the roman numeral

    for val, s in data.items():
        while num >= val:   # dividing the num multiple time until it become smaller than the value
            roman += s  # adding the roman numeral to result
            num -= val  # decriseing the num by value
            
    # handling the special cases
    roman = roman.replace('DCCCC', 'CM')  # 900
    roman = roman.replace('CCCC', 'CD')   # 400
    roman = roman.replace('LXXXX', 'XC')  # 90
    roman = roman.replace('XXXX', 'XL')   # 40
    roman = roman.replace('VIIII', 'IX')  # 9
    roman = roman.replace('IIII', 'IV')   # 4

    return roman


def int_to_roman2(num: int) -> str:
    data = {1000:'M',
         900:'CM', 
         500:'D', 
         400:'CD',
         100:'C',
         90:'XC', 
         50:'L', 
         40:'XL',
         10:'X',
         9:'IX',
         5:'V',
         4:'IV', 
         1:'I'
        }   # dictionary to store the roman values
    
    roman = ''  # to store the roman numeral

    for val, s in data.items():
        while num >= val:   # dividing the num multiple time until it become smaller than the value
            roman += s
            num -= val

    return roman

print(int_to_roman(3749))
print(int_to_roman2(3749))
print(int_to_roman(58))
print(int_to_roman2(58))
print(int_to_roman(1994))
print(int_to_roman2(1994))
         
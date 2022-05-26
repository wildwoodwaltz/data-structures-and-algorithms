def numeral_converter(numeral):
    """
    Function Takes in a string of roman numerals and converts them to arabic numerals
    """
    arabic_number = 0

    for idx in range(len(numeral) - 1):

        left_num = numeral[idx]
        right_num = numeral[idx + 1]

        left_val = convert(left_num)
        right_val = convert(right_num)

        if left_val < right_val:
            left_val = -left_val

        arabic_number += left_val
    
    if numeral:
        arabic_number += convert(numeral[-1])

    return arabic_number

def convert(rom_num):
    legend = {
        "M": 1000, 
        "D": 500, 
        "C": 100, 
        "L": 50, 
        "X": 10, 
        "V": 5, 
        "I": 1
        }
    
    return legend.get(rom_num,0)

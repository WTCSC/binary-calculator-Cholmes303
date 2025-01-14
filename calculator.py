# Calculator for binary numbers
def binary_calculator(bin1, bin2, operator):
    
    # Checks each given arguement to be binary.
    for character in bin1:
        if character not in ["0", "1"]: 
            return "Error"
    for character in bin2:
        if character not in ["0", "1"]:
            return "Error"
    
    # Adds extra zeros to given binary digits to ensure all values are 8 bit.
    if len(bin1) < 8:
        bin1 = bin1.zfill(8)
    if len(bin2) < 8:
        bin2 = bin2.zfill(8)
    
    decimal_bin1 = 0
    decimal_bin2 = 0

    # Loop to convert binary numbers into decimal values.
    for index, value in enumerate(bin1):
        if value == "1":
            decimal_bin1 += 2 ** (7 - index)
    
    for index, value in enumerate(bin2):
        if value == "1":
            decimal_bin2 += 2 ** (7 - index)
    
    # Decimal value of both binary numbers.
    decimal_value = 0

    # Checks the given operator and performs the calculation.
    if operator == "+":
        decimal_value += decimal_bin1 + decimal_bin2

    elif operator == "-":
        decimal_value += decimal_bin1 - decimal_bin2

    elif operator == "*":
        decimal_value += decimal_bin1 * decimal_bin2
    
    elif operator == "/":
        if decimal_bin2 == 0:
            return "Nan"
        decimal_value += decimal_bin1 / decimal_bin2

    # Checks if the decimal value is within the 8 bit range.
    if decimal_value < 0 or decimal_value > 255:
        return "Overflow"

    output = ""

    bit_8 = [128, 64, 32, 16, 8, 4, 2, 1]
    
    # Converts the decimal value back to binary.
    for bit in bit_8:
        if decimal_value >= bit:
            output += "1"
            decimal_value -= bit
        else:
            output += "0"
    return(output)
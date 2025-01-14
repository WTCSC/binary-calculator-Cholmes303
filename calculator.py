# Calculator for binary numbers.
def binary_calculator(bin1, bin2, operator):
    
    # Checks each given arguement to be binary numbers.
    for character in bin1:
        if character not in ["0", "1"]: 
            return "Error"
    for character in bin2:
        if character not in ["0", "1"]:
            return "Error"
        
    decimal_bin1 = 0
    decimal_bin2 = 0

    # Converts binary numbers into decimal values. Index counts the position of the binary number to account its value. 
    for index, value in enumerate(bin1):
        # Allows for any length input, subtracts one due to len() function starting at 1 instead of 0. 
        bin1_len = len(bin1) - 1
        if value == "1":
            # Math function used make base 2 into base 10 (binary value + 2^x).
            decimal_bin1 += 2 ** (bin1_len - index)
    
    for index, value in enumerate(bin2):
        # Allows for any length input, subtracts one due to len() function starting at 1 instead of 0.
        bin2_len = len(bin2) - 1
        if value == "1":
            # Math function used make base 2 into base 10 (binary value + 2^x).
            decimal_bin2 += 2 ** (bin2_len - index)
    
    # Decimal value of both binary numbers.
    decimal_value = 0

    # Checks the given operator and performs the calculation.
    # Adds both numbers together.
    if operator == "+":
        decimal_value += decimal_bin1 + decimal_bin2

    # Subtracts the second number from the first number. 
    elif operator == "-":
        decimal_value += decimal_bin1 - decimal_bin2

    # Multiplies both numbers together. 
    elif operator == "*":
        decimal_value += decimal_bin1 * decimal_bin2
    
    # Divides the first number by the second number. 
    elif operator == "/":
        # Checks for dividing by zero, undefined solution. 
        if decimal_bin2 == 0:
            return "NaN"
        decimal_value += decimal_bin1 / decimal_bin2

    # Checks if the decimal value total is in the 8 bit range (0-255).
    if decimal_value < 0 or decimal_value > 255:
        return "Overflow"

    output = ""

    bit_8 = [128, 64, 32, 16, 8, 4, 2, 1]
    
    # Converts the decimal value back to binary.
    for bit in bit_8:
        # Compares decimal value and when over flowed adds one to output and then subtracts decimal from bit to move to next digit place. 
        if decimal_value >= bit:
            output += "1"
            decimal_value -= bit
        else:
            output += "0"
    return(output)

# Print statement for people using the calculator. 
#print(binary_calculator("0000", "0000", "+"))
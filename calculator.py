# Timer for funsies
import time

# Calculator for binary numbers
def binary_calculator(bin1, bin2, operator):
    
    # Checks each given arguement to be binary
    for character in bin1, bin2:
        if character == "0" or "1":
            pass
        else:
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
    
    # Variable for output.
    answer = 0

    # If statements for all operator usage.
    if operator == "+":
        answer += decimal_bin1 + decimal_bin2

    if operator == "-":
        answer += decimal_bin1 - decimal_bin2

    if operator == "*":
        answer += decimal_bin1 * decimal_bin2
    
    if operator == "/":
        answer += decimal_bin1 / decimal_bin2


    output = []
    bit_8 = [128, 64, 32, 16, 8, 4, 2, 1]

    for x in bit_8:
        if (answer / x) >= 1:
            output.append("1")
        elif (answer / x) <= 1:
            output.append("0")
    output = ''.join(output)
        
    print(output)
    #print(decimal_bin1, decimal_bin2)
    

#binary_calculator("0001", "0011", "+")

if __name__ == "__main__":
    start_time = time.time()
    print(binary_calculator("1010", "0101", "+"))
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.10f} seconds")

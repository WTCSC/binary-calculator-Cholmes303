[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17648539)

<!--

The following requirements must be met to receive full credit on this assignment. The calculator must handle binary arithmetic operations accurately while following proper error handling procedures and output formatting guidelines.

- Your solution must have a well-written and thorough README file.
- The solution must be implemented as a function called `binary_calculator()` with three parameters:
    - `bin1` - A string parameter representing the first binary number to be used in the calculation. Must contain only 0s and 1s.
    - `bin2` - A string parameter representing the second binary number to be used in the calculation. Must contain only 0s and 1s.
    - `operator` - A string containing one of the following arithmetic operators: `'+'`, `'-'`, `'*'`, or `'/'`
- Do not use Python's built-in `bin()` function.
- Implement your own binary-to-decimal and decimal-to-binary conversion logic.
- All binary inputs and outputs should be strings.
- Handle division by zero by returning `"NaN"`
- Handle decimal numbers by rounding down to the nearest whole number (flooring).
- Return `"Error"` for invalid binary inputs (containing characters other than `0` and `1`)
- Return `"Overflow"` for any operations that overflow (i.e. negative numbers, numbers greater than 8-bits).
- Outputs must be returned as 8-bit numbers (padded with leading zeros if necessary). For example, the decimal number `5` should be returned as `"00000101"` .

Your solution will be tested against various test cases including edge cases, invalid inputs, and all four arithmetic operations.

 -->

 # Binary Calculator

This project is a binary calculator. The code works by having three given arguemnts, the first two being numbers in binary notation, and additionally one of the four operations (addition, subtraction, multiplication, and division). Once these inputs are given an output of the calculated binary number will be given, however there are exceptions to this calculator. This calculator operates in 8 bits meaning it will not given a negative or output greater than 255. Furthermore, if any number is not given in binay notation or the second number is zero and being divided, the calculator will return "Error" or "Nan". 



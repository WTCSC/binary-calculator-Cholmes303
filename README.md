[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17648539)

# Binary Calculator

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

## Introduction

This is a calculator that is used for binary calculations. This is written in the Python programming language and will return 8 bit values (0-255 in decimal value). To use the calculator 3 arguements are required, the first two are binary numbers and the final arguement is the operation that will be used (addition, subtraction, multiplication, division). The calculator will account for errors like outputs that are greater than 8 bit, incorrect arguements, and dividing by zero. 

### Requirements to run program

The Python programming language is required for this program to run. Head over to [Python's official website](https://www.python.org/downloads/) and download the correct version of Python for your machine. 

#### Installation

To install this program the GitHub repository will need to be cloned down to your machine. To do this open a terminal. Then use the command:
```
git clone <repository URL>
```
Replace the ```<repository URL>``` with the GitHub repository that is going to be cloned. 

##### Start Up

Now that the code is cloned onto your machine, you can run the program. Before running the code open up the calculator.py file and remove the ```#``` from the print statement on line 69. Next change the arguements within the print statement to have the desired binary numbers and operator that is going to be used. Once all of this is set up the file may be run to calculate your binary number. To run the program open up a terminal and navigate to the correct directory that contains the calculator.py file. This will most likely be in the binary-calculator folder. Once in the correct directory use the command to run the program. 
```
python3 calculator.py
```

###### Trouble Shooting

Problems may occur when cloning the repository. If an error with configuring user.name and user.email occurs, use the commands to configure your GitHub username and email:
```
git config --global user.name "Your Name"
```
```
git config --global user.email "Your Email"
```
Replace the quotation sections in the command with your name and email.
For more trouble shooting with cloning GitHub repositories head to [GitHub's website](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
When cloning the repository make sure you know where you are cloning the repository. This is found when you are in the terminal on your machine.  




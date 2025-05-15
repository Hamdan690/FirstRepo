firstNumber = int(input("Enter a number: "))
secondNumber = int(input("Enter the second number: "))
sign = input("which sign do you want? ")


if sign == "+":
    Add = firstNumber + secondNumber
    print(f'{firstNumber} + {secondNumber} = {Add}')
elif sign == "-":
    Subract = firstNumber - secondNumber
    print(f'{firstNumber} - {secondNumber} = {Subract}')
elif sign == "*":
    Multiply = firstNumber * secondNumber
    print(f'{firstNumber} * {secondNumber} = {Multiply}')
elif sign == "/":
    Divide = firstNumber // secondNumber
    print(f'{firstNumber} / {secondNumber} = {Divide}')
elif sign == "%":
    Percentage = firstNumber % secondNumber
    print(f'{firstNumber} % {secondNumber} = {Percentage}')
else:
    print("That's not a sign!")
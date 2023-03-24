#Console calculator
import math

doAgain = True

try:
    while doAgain == True:
        firstNumber = 0
        secondNumber = 0
        result = 0
        doAgain = True

        print("Enter first number: ")
        firstNumber = float(input())
        print("For addition enter: \"+\"" +
            "\nFor subtraction enter: \"-\"" +
            "\nFor multiplication enter: \"*\"" +
            "\nFor division enter:  \"/\"" +
            "\nFor the root enter: \";\"" +
            "\nFor calculate the power enter: \"^\"")
        operation = input()
        if operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != ';' and operation != '^':
            raise Exception("Wrong data!")

        if operation != ';':
            print("Enter second number: ")
            secondNumber = float(input())

        if operation == '+':
            result = firstNumber + secondNumber
        if operation == '-':
            result = firstNumber - secondNumber
        if operation == '*':
            result = firstNumber * secondNumber
        if operation == '/':
                if secondNumber == 0:
                    raise Exception("YOU CAN'T DIVIDE BY 0!")
                result = firstNumber / secondNumber
        if operation == ';':
            result = math.sqrt(firstNumber)
        if operation == '^':
            result = math.pow(firstNumber, secondNumber)

        if operation == ';':
            print("Square root of: " + str(firstNumber) + " = " + str(result))
        elif operation == '^':
            print("Power of: " + str(firstNumber) + operation + str(secondNumber) + " = " + str(result))
        else:
            print("Result of: " + str(firstNumber) + " " + operation + " " + str(secondNumber) + " " + " = " + str(result))

        print("Do you want to do another math operation (Y/N)")
        anotherOperation = input()
        anotherOperation = anotherOperation.upper()

        if anotherOperation == "Y":
            doAgain = True
        elif anotherOperation == "N":
            doAgain = False
        else:
            raise Exception("Entered data is wrong!")
    print("Calculator has been closed!")
except:
    print("An exception occurred")


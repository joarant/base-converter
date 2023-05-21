import math 

def convertToDecimal(numbers: str,base: int):
    sum = 0
    numbersSplit = numbers.split(".")
    for i in range(0,len(numbersSplit[0])):
            sum += int(numbersSplit[0][i]) * math.pow(base, len(numbersSplit[0]) - i -1)
    if len(numbersSplit) == 2:
        for i in range(0,len(numbersSplit[1])):
            sum += int(numbersSplit[1][i]) * math.pow(base,- i -1)
    print(sum, "sum")
    
    return sum



def convertDecimalToBase(numbers: str, base: int):
    print(numbers, "numbers")

    numberString = ""
    numbersSplit = numbers.split(".")

    quotient = int(numbersSplit[0])
    while(quotient != 0):
        numberString = str(quotient % base) + numberString
        quotient = math.floor(quotient / base)
    if len(numbersSplit) == 2:
        decimalCounter = 0
        number = str(float("0."+ numbersSplit[1]) * base).split(".")
        decimalNumberString = number[0]

        while(decimalCounter < 5):
            number = str(float("0."+ number[1]) * base).split(".")
            decimalNumberString += number[0]
            decimalCounter+=1
        return numberString + "." + decimalNumberString
    
    return numberString

def convert(numbers: str, baseFrom: int, baseTo: int):
    sign = ""
    if "-" in numbers:
        sign = "-"
        numbers = numbers.replace("-","")

    if baseFrom == 10:
        return sign + convertDecimalToBase(numbers, baseTo)
    else:
        return sign + convertDecimalToBase(str(convertToDecimal(numbers, baseFrom)), baseTo) # from base -> decimal -> to base



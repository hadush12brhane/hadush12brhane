import math
def decimal_to_binary(n):
    if n == 0:
        return '0'
    
    decimal, integ = math.modf(n)
    binary = ''
    while integ > 0:
        binary = str(int(integ) % 2) + binary
        integ //= 2
    if decimal!=0:
        binary =  binary + '.'
        for i in range(10): # binary representation of floats to 10 significant figuire
            decimal = round(decimal,10) *2
            decimal,b = math.modf(decimal)
            binary =   binary + str(int(b))
            if decimal ==0:
               break
    return binary

decimal_number = float(input("enter the nubmer"))
binary_number = decimal_to_binary(decimal_number)
print("Binary representation of", decimal_number, "is", binary_number)



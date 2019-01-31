#1SELECT FOUR BINARY ARITHMETIC OPERATORS
#2FOR EACH OPERATOR::RANDOMLY GENERATE TWO NUMBERS AND OPERATE ON THEM
#DO 2 THREE TIMES   

#Uploaded to Git
import random

print("\nAvailable operators\n")
print("\n1.addition         :: + ")
print("\n2.Subtraction      :: - ")
print("\n3.Division         :: / ")
print("\n3.Multiplication   :: * ")

combinedResults = []

def addition():
    
    addend = random.randint(1, 100)
    annuend = random.randint(1, 100)
    sum = addend + annuend
    print(f"{addend} + {annuend} = {sum}")
    combinedResults.append(sum)
    print(combinedResults)
    

def subtract():
    
    minuend = random.randint(1, 100)
    subtrahend = random.randint(1, 100)
    difference = minuend - subtrahend
    print(f"{minuend} - {subtrahend} = {difference}" )
    combinedResults.append(difference)
    


def divide():
    
    dividend = random.randint(1, 100)
    divisor = random.randint(1, 100)
    quotient = dividend / divisor
    quotient = round(quotient, 3)
    print(f"{dividend} / {divisor} = {quotient}")
    combinedResults.append(quotient)


def multiply():
    
    muliplicand = random.randint(1, 100)
    multiplier = random.randint(1, 100)
    product = muliplicand * multiplier
    print(f"{muliplicand} + {multiplier} = {product}" )
    combinedResults.append(product)
    

numberOfTimes = int(input(print("\nHow many times do you want to do each operation?\n:")))

print("\n****ADDITION****")
for times in range(0, numberOfTimes):
    addition()

print("\n****SUBTRACTION****")
for times in range(0, numberOfTimes):
    subtract()

print("\n****DIVISION****")
for times in range(0, numberOfTimes):
    divide()

print("\n****MULTIPLICATION****")
for times in range(0, numberOfTimes):
    multiply()


print(f"\nResults: {combinedResults}")
combinedResults.sort()
print(f"\nSorted results: {combinedResults}")








    

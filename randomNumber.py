
from secrets import randbelow

print("\n Card choices")
print("\n0-12 spade")
print("\n13-25 hearts")
print("\n26-38 diamonds")
print("\n39-52 clubs")

x = randbelow(52) 
y = randbelow(52) 
z = randbelow(52) 
m = randbelow(52) 

print("\n**********************\n")

for x in [x, y, z, m]:
    print(x)

    if(x >= 0 and x<= 12):
        print("Card is Spade")

    elif(x >= 13 and x<= 25):
        print("Card is Heart")

    elif(x >= 26 and x<= 38):
        print("Card is Diamond")

    else:
        print("Card is Club")
        
print("\n**********************\n")


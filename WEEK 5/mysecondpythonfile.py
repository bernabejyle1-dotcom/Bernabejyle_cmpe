intLength = len(strFullName)
print(intLength)
print(strFullName[0])
print(strFullName[5])
print(strFullName[intLength - 1])

strInputFromUser = "Marcos"

strFuName = strInputFromUser
print(strFullName)
intLength = len(strFullName)
print(intLength)

strFullName = "leonel calderon"


strNewValue = strFullName.upper()
print(strNewValue)

strNewValue = strFullName.count("e")
print(strNewValue)

strNewValue = strFullName.split(" ")
print(strNewValue)


strFirstName = "Jyle"
strMiddleName = "Lebron"
strLastName = "James"
strFullName = "_".join([strFirstName, strMiddleName, strLastName])
print(strFullName)

newValue = strFullName.isnumeric()
print(newValue)

newValue = strFullName[2:9]
print(newValue)
newValue = strFullName[2:9:2]
print(newValue)

print(strFullName.index("e"))



myIntegerA = 25
myIntegerB = 15
myFloatA = 25.45
myFloatB = 13.25
myComplexNumberA = 25 - 3j
myComplexNumberB = 10 - 12j

mySum = myIntegerA + myIntegerB
print(mySum)
myDiff = myIntegerA - myIntegerB
print(myDiff)
myProd = myIntegerA + myIntegerB
print(myProd)
myQo = myIntegerA / myIntegerB
print(myQo)

remainder = myIntegerA % myIntegerB
print(remainder)
remainder = myIntegerA % myIntegerB
print(remainder)

myComProd = myComplexA * myComplexB
print(myComProd)

print(5*4*3*2*1)
print(math.factorial(5))



isNumeric = False
myChar = "6"

isNumeric = myChar.isnumeric()
strIsNumeric = str(myChar.isnumeric())
print(isNumeric)
print([strIsNumeric])

a = 10
b = 20

isEqual = (a == b)
print(isEqual)
isEqual = (a <= b)
print (isEqual)
isEqual = (a >= b)
print(isEqual)

result = 2*5
print(result)

#in, not, in is

isIn =(5 in [10, 20, 30, 40, 50])
print(isIn)
isIn =(5 in [10, 20, 30, 40, 50])
print(isIn)

isIs = ("hello daddy" is "hello mommy")
print(isIS)
isIs = ("hello daddy" is "hello mommy")
print(isIs)

isOkay = (5 in [10, 20, 30, 40, 50] and (5 in [10, 20, 30, 40, 50]
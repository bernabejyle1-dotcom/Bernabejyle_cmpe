shapeofyou = input("Enter shape of you")

if shapeofyou == "circle" :
    print("circle")
elif shapeofyou == "square" :
    print(square)
elif shapeofyou == "triangle" :
    print(triangle)
else:
    print("baby")

    print("Next question")


----------------------------------------------------------------------------------------------------------------------
    myGrade = float(input("Enter your grade: "))

    if myGrade >= 97:
        print("Grade is greater than 1.0")

    elif myGrade >= 94:
        print("Grade is greater than 1.25")

    elif myGrade >= 91:
        print("Grade is greater than 1.50")

    elif myGrade >= 88:
        print("Grade is greater than 1.75")

    elif myGrade >= 85:
        print("Grade is greater than 2.00")

    elif myGrade >= 82:
        print("Grade is greater than 2.25")

    elif myGrade >= 79:
        print("Grade is greater than 2.50")

    elif myGrade >= 76:
        print("Grade is greater than 2.75")

    elif myGrade >= 75:
        print("Grade is greater than 3.00")

    else:
        print("5.0/INC/W/D")

----------------------------------------------------------------------------------------------------------------------
    citizenship = "filipino"
    age = 18
    registered = True

    if citizenship == "Filipino" and age >= 18:
        if registered:
            print("you can vote")
        else:
            print("you can not vote but you can register now")
    elif citizenship == "Filipino" and age < 18:
        print("you cannot vote. Please wait until you are eligible and then register.")
    else:
        print("you can not vote nor register")


-----------------------------------------------------------------------------------------------------------------------





print("before loop")

for x in range(0, 10, 1):
    print("x value is : " + str(x))

print("after loop")

for x in range(10):
    print("x values is :" + str(x))

print("after loop")
print("before loop")





print("before loop")

for x in range(5, 30, 3):
    print("x value is : " + str(x))

print("after loop")


--------------------------------------------------------------------------------------------------------------------

fruitslist = ["Apple", "Banana", "Cherry"]

for fruit in fruitslist:
    print("fruit list include : " + fruit)

print("After Loop")

mString = "hajshajdhjhdakdhdkg"
for char in mString:
    print(char.upper())

print("After Loop")
#kahit anong name pede

# ------------------------------------------------------------------------------------------------------------------------

originalValue = "daddy robbbbb"
newValue = ""

for x in originalValue:
    n
ewValue = x + newValue

print("new value : " + newValue)

print("before loop")

for i in range(10):
    if i % 2 == 0:
        print("even numbers : " + str(i))
        continue
    elif i > 6:
        print("i is greater than 6")
        break
    print("i value npw is : "
    str(i))
    print("after loop")

    -----------------------------------------------------------------------------------------------------------------

    import time

    isConnected = "ugh"

    for retry in range(4):
        time.sleep(2)
        isConnected = input("Is connected?")
        if isConnected == "daddy":
            print("Now Connected")
            break
        else:
            print("Request time out.")

    print("Processing your request . . .")

    -------------------------------------------------------------------------------------------------------------------
    # nested loop - loop within the loop

    for i in range(10):
        print(str(i) + "====================="
              for x in range(10):
        print(x)

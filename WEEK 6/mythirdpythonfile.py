fruitsA = ["apple", "apple", "banana", "orange", "mango"]
print(fruitsA)
print(fruitsA[2])
print(fruitsA.index("banana"))
isthere = "orange" in fruitsA
print(isthere)

fruitsA.append("dragon fruit",)
print(fruitsA)
fruitsA.insert(2, "durian")
print(fruitsA)
print(len(fruitsA))
print(fruitsA.count("Apple"))
fruitsA.remove("apple")
print(fruitsA.index("banana"))


fruitsA = ["apple", "apple", "banana", "orange", "mango"]
fruitsB = ["lychee", "watermelon", "lychee", "katkat", "watermelon"]
fruitsC = ["rambutran", "grapes", "grapes", "pineapple", "papaya"]


fruitBasket_list = [fruitsA, fruitsB, fruitsC]
print(fruitBasket_list)
print(fruitBasket_list[2])
print(fruitBasket_list[1][3])


fruitBasket_Plus = fruitsA + fruitsB + fruitsC
print(fruitBasket_Plus)

fruitsA.extend(fruitsB)
fruitsA.extend(fruitsC)
print(fruitsA)



fruitsA =("apple", "apple", "banana", "orange", "mango")
print(fruitsA)

print(fruitsA.index("banana"))
print(fruitsA.count("apple"))

print(fruitsA[4])

fruitsB =("lychee", "watermelon", "lychee", "katkat", "watermelon")
fruitsBasket = (fruitsA, fruitsB)
print(fruitsBasket)


myTuple = (
 (4, 3, 2, "A")
 (5, 6, 7,"B")
 (8, 9, 10,"C")
 (11, "*", "H", "D"),
)
print(mytuple[3][2])

print(myInfo)
print(myInfo["Name"])
print(myInfo["Age"])
print(myInfo.get("Name"))
myInfo["Name"] = "Marck kwn"
print(myInfo)
print(myInfo["Name"])
myInfo.update({"section" : 2})
print(myInfo)


myInfo = {"Name" : "Jyle Mathiue", "Age" : 18, "Citizenship" : "Canadian", "Province" : "Bulacan City"}
print(myInfo)
print(myInfo["Name"])
print(myInfo["Age"])
print(myInfo["Citizenship"])
print(myInfo["Province"])
myInfo["Name"] = "lebrong jims"
print(myInfo)
print(myInfo["Name"])
myInfo.update({"Section" : 4})
print(myInfo)




myInfo = { "Name" : "Jyle Mathiue",
           "Age" : 18, "Gender" : "Male",
           "Citizenship" : "Canadian",
           "Address" : "City of Mandalyuong",
           "Hobbies" : ["study, study, study until i die"]

}
print(myInfo)
print(myInfo["Hobbies"])
print(myInfo["Hobbies"][1])


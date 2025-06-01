#Dictionaries and Tuples


#Tuple

#Ordered ImmutableCollection pf Element


# Score = (1,2,3,4,5,6)
# friends = ("Yann","Rohan","Adnan","Arghay","Rupantar","Kaisan")


# #Acsess Element

# print(friends)
# print(friends[2])

# #Length - Number of items inside your tuple
# print (len(friends))


# #Membership
# print("Rohan" in friends)
# print("Talha" in friends)

#Dictionaries - Key-Value   List = []Tuple = Dist{}

Phonebook = {

    "Shomopriyo" : 89564273115 ,
    "Yann" : 8162944354 ,
    "Rohan" : 846832517966 ,
    "Kaisan" : 87553168942 ,


}


#print (Phonebook)

#All Keys / Values
print(Phonebook.keys())
print(Phonebook.values())

#Acsess Element
print(Phonebook.get("Shomopriyo"))
print(Phonebook.get("Yann"))
print(Phonebook["Rohan"])

#Updates
Phonebook["Kaisan"] = 866677921
print(Phonebook.get("Kaisan"))


#Removes

del Phonebook["Kaisan"]
print(Phonebook)

#Add

Phonebook['Arghay'] = 8223564497
print(Phonebook)

#loops

for names in Phonebook :
    print(names)

for key , value in Phonebook.items() :
    print(key, value)




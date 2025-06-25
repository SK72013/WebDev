friends = open("Myfriend.txt","w")

friends.write("Tawaf\n")
friends.write("Yann\n")
friends.write("Rohan\n")
friends.write("Adnan")
friends.close()

friends = open("Myfriend.txt","a")

friends.write("Evan\n")
friends.write("Tawhid\n")
friends.write("Araf\n")
friends.write("Argaya")
friends.close()

# friends = open("Myfriend.txt","r")
# content = friends.read()
# print(content)

friends = open("Myfriend.txt","r")
first_line = friends.readline()
print(first_line)
guests = ["Will Smith", "Ben Aflick", "Anjelina Jolie"]
print("I'am sorry, but i can invite only 2 guests")
print("Deear "  + (guests[0]),  "can you accept my invite for dinner")
print("Deear "  + (guests[1]),  "can you accept my invite for dinner")
print("Deear "  + (guests[2]),  "can you accept my invite for dinner")
guests.pop(1)
guests.insert(1, "Katrin")
guests.insert(0, "Michael Jordan")
guests.insert(2, "Steven Jobs")
guests.append("Irina Sheykh")
guests.pop(1)
print("i'am really sorry, Will you cannot come")
guests.pop(0)
print("i'am really sorry, Ben you cannot come")
guests.pop(1)
print("i'am really sorry, Steven you cannot come")
print("Deear "  + (guests[1]),  "can you accept my invite for dinner")
print("Deear "  + (guests[2]),  "can you accept my invite for dinner")
del guests[:]
print(guests) 
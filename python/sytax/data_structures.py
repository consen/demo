# ****************************************************************** #
# ************************* Byte of Python ************************* #
# ****************************************************************** #

########################
# using_list
########################
# shoplist = ["apple", "mango", "carrot", "banana"]

# print("I have", len(shoplist), "items to purchase.")

# print("These items are:", end = " ")
# for item in shoplist:
# 	print(item, end = " ")

# print("\nI also have to buy rice.")
# shoplist.append("rice")
# print("My shopping list is now", shoplist)

# print("I will sort my list now")
# shoplist.sort()
# print("Sorted shopping list is", shoplist)

# print("The first item I will buy is", shoplist[0])
# olditem = shoplist[0]
# del shoplist[0]
# print("I bought the", olditem)
# print("My shopping list is now", shoplist)

########################
# using_tuple
########################
# zoo = ("python", "elephant", "penguin")
# print("Number of animals in the zoo is", len(zoo))

# new_zoo = "monkey", "camel", zoo
# print("Number of cages in the new zoo is", len(new_zoo))
# print("All animals in new zoo are", new_zoo)
# print("Animals brought from old zoo are", new_zoo[2])
# print("Last animal brought from old zoo is", new_zoo[2][2])
# print("Number of animals in the new zoo is", len(new_zoo) - 1 + len(new_zoo[2]))

########################
# using_dict
########################
# ab is short for addressbook
# ab = {
# 	"Swaroop"  : "swaroop@swaroopch.com",
# 	"Larry"    : "larry@wall.org",
# 	"Matsumoto": "matz@ruby-lang.org",
# 	"Spammer"  : "spammer@hotmail.com"
# }

# print("Swaroop's address is", ab["Swaroop"])

# del ab["Spammer"]
# print("\nThere are {0} contacts in the address-book\n".format(len(ab)))

# for name, address in ab.items():
# 	print("Contact {0} at {1}".format(name, address))

# ab["Guido"] = "guido.python.org"

# if "Guido" in ab:
# 	print("\nGuido's address is", ab["Guido"])


########################
# seq
########################
# shoplist = ["apple", "mango", "carrot", "banana"]
# name = "swaroop"

# print("Item 0 is", shoplist[0])
# print("Item 1 is", shoplist[1])
# print("Item 2 is", shoplist[2])
# print("Item 3 is", shoplist[3])
# print("Item -1 is", shoplist[-1])
# print("Item -2 is", shoplist[-2])
# print("Character 0 is", name[0])
# print("Character -1 is", name[-1])

# print("Item 1 to 3 is", shoplist[1:3])
# print("Item 2 to end is", shoplist[2:])
# print("Item 1 to -1 is", shoplist[1:-1])
# print("Item start to end is", shoplist[:])

# print("characters 1 to 3 is", name[1:3])
# print("characters 2 to end is", name[2:])
# print("characters 1 to -1 is", name[1:-1])
# print("characters start to end is", name[:])


########################
# set
########################
# bri = set(["brazil", "russia", "india"])
# "india" in bri
# "usa" in bri

# bric = bri.copy()
# bric.add("china")
# bric.issuperset(bri)

# bri.remove("russia")
# bri & bric


########################
# reference
########################
# print("Simple Assignment")
# shoplist = ["apple", "mango", "carrot", "banana"]
# mylist = shoplist

# del shoplist[0]

# print("shoplist is", shoplist)
# print("mylist is", mylist)

# print("\nCopy by making a full slice")
# mylist = shoplist[:]
# del mylist[0]

# print("shoplist is", shoplist)
# print("mylist is", mylist)

# print("\nSimple object")
# five = 5
# five2 = five
# five2 = 6
# print("five is", five)
# print("five2 is", five2)


########################
# str_methods
########################
# name = "Swaroop"

# if name.startswith("Swa"):
# 	print("Yes, the string starts with 'Swa'")

# if "a" in name:
# 	print("Yes, it contains the string 'a'")

# if name.find("war") != -1:
# 	print("Yes, it contains the string 'war'")

# delimiter = "_*_"
# mylist = ["Brazil", "Russia", "India", "China"]
# print(delimiter.join(mylist))


########################
# list comprehension
########################
leaps = [y for y in range(1900, 1940)
		if (y % 4 ==0 and y % 100 != 0) or (y % 400 == 0)]
print(leaps)

codes = [s + z + c for s in "MF" for z in "SMLX" for c in "BGW"
		if not (s == "F" and z == "X")]
print(codes)
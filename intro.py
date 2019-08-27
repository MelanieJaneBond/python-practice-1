my_list = ["good", "morning", 4, False, [3,6,9], {"thing": "bag"}]

my_list.append("friends")
print(my_list)

list_copy = my_list.copy()
print(list_copy)
# You'd use this if you wanted to make changes to the list and
# use it in your app somewhere without altering the original.
# Maybe if you were going to sort it or filter it somehow

my_new_list = list("hey")
print(my_new_list)

my_new_list_again = list(["hey"])
print(my_new_list_again)

print("count", my_list.count([3,6,9]))

# Dictionary
my_pairs = {
    "name": "Fred",
    "age": 46
}
print(my_pairs)

name = my_pairs["name"]
print(name)

my_pairs["last"] = "Jones"
print(my_pairs)
my_pairs["address"] = {"street": "123 Sesame St", "zip": 40503}
print(my_pairs)
print(my_pairs["address"]["zip"])

print("items", my_pairs.items())
print("values", my_pairs.values())

print("Here's where the line breaks, Melanie")

for foo in my_pairs.items():
    print(foo)

for key,value in my_pairs.items():
    print(value)
# this will print the items in the dictionary "my_pairs"
#the part where you state key,value tells it to label the
#items as a key first and then a value, then, you tell it
# to print only the value items
print(f'Hello, my name is {my_pairs["name"]}')

my_set = {"fred", 3, 12, True, "Jones", 3}
print("set", my_set)
my_dupes = [1,2,3,4,2,5,1]
my_dupes = set(my_dupes)
print(list(my_dupes))
#when you use a "set", Python WILL NOT print the same
#value twice.
#Also! Note that we turned a list into a set and then turned
#that set back into a list.
my_set.add("hello C33")
print(my_set)

my_tup = ("1", 1, 3, "Hello", True, 3)
print(my_tup)
print(my_tup.count(3))
print(my_tup.index("Hello"))

print("NEW SECTION IN THE LESSON, MELANIE!!!")

name = "Stebe"
if name is not "Stebe":
    print("I feel good")
elif name == "Joe":
    print("Joe is the King of the World")
else:
    print("I have a cold")
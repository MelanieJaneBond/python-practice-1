zoo = ("parrot", "zebra", "elephant", "bald_eagle", "python", "gecko", "kangaroo", "bonobo", "penguin", "beaver")
print(zoo.index("elephant"))

animal_to_find = "kangaroo"
if animal_to_find in zoo:
    print(f"I found the {animal_to_find}")

zoo_as_list = [zoo]
print(zoo_as_list)

three_more_animals = ["lion", "tiger", "bear"]
zoo_as_list.extend(three_more_animals)
print(f"Extended List : ", zoo_as_list)

back_to_tuple = (zoo_as_list)
print(back_to_tuple)
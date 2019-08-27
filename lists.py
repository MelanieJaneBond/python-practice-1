import random
# each number will be between 0 and 6.

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1,6,1))

different_numbers = [1,2,3,4,5,6,7,8,9,10]

for i in different_numbers:
    if my_randoms.count(i) == True:
        print(f"my_randoms list contains {i}")
    elif my_randoms.count(i) == False:
        print(f"my_randoms does not contain {i}")

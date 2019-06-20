list = ['a', 'A', 'c', 'D', 'e']

new_item1 = input("Please enter a list item: ")
new_item2 = input("Please enter another list item: ")

list.append(new_item1)
list.append(new_item2)

print(list)

print("Popping off the first item in the list")

list.pop(0)

print(list)

print("The length of the list is {}.".format(len(list)))

list.sort()

print("Sorting the list...")

print(list)

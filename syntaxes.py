my_info = ('mike', 24, 'programmer')
# Tuple is immutable
print(my_info[1])


one_element_tuple = (4,)
print(one_element_tuple)

# zip()
# combining two lists into one

owners = ["Jenny", "Alexus", "Sam", "Dog"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"] # if dimension does not match, dropping the rest
owners_and_dogs_names = zip(owners, dogs_names)
new_list = list(owners_and_dogs_names)
print(new_list)
print(type(new_list[0]))
new_list.append(["hey", "haha"])
print(new_list)
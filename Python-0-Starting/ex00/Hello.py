ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"  # a list can be modified by index
ft_tuple = ("Hello", "France!")
# Once a tuple is created, you cannot change its values.
# Tuples are unchangeable, or immutable
ft_set.remove("tutu!")
ft_set.add("Paris!")
# Sets are a type of data structure that stores unique elements.

ft_dict["Hello"] = "42Paris!"
# Dictionaries are used to store data values in key:value pairs.

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

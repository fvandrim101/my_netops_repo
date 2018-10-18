my_dictionary = {}
print (type(my_dictionary))
my_dictionary["gigE0"] = "Link to ISP"
print(my_dictionary)
my_dictionary["gigE1"] = "DNS is the root of all problems"
my_dictionary["gigE2"] = "An IPv4 address walks into the bar and yells, 'Bartender! Give me a Cider, I'm exhausted!"
my_dictionary["gigE3"] = "You know the thing about all NTP jokes? It's all about the timing!"
print(my_dictionary)
print(my_dictionary["gigE0"])
my_other_dictionary = {}
my_other_dictionary ["master_key"]="zeus"
print(my_other_dictionary)
# my_dictionary ["nested_list"] = my_list
my_dictionary ["nested_dict"] = my_other_dictionary
print(my_dictionary)
print(my_dictionary["nested_dict"]["master_key"])

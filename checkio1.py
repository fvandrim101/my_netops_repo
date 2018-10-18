
import re
data = "A1213pok1A"
print(data)
print()
# print (len(data) > 10)
# print()
#
# print(type(10==10))
# print(10==10)
#
# print("Space")
#
#
digit = re.compile ('\d')
lowercase = re.compile ("[a-z]")
uppercase = re.compile ("[A-Z]")
dummy = True
# print()

if (len(data) < 10):
#    print("too short")
    dummy = False
elif not (digit.search(data)):
#    print("no digit")
    dummy = False
elif not (lowercase.search(data)):
#    print("no lower")
    dummy = False
elif not (uppercase.search(data)):
#    print("no upper")
    dummy = False

print(dummy)
#    print("good combo")

#print()
# print (type(dummy))
#print(dummy)
# return must be within function, placed here for notation, not execution in testing
#  return(dummy)

import sys
Value = input("Enter any value: ")

print("Value           :", Value)
print("Data Type       :", type(Value))
print("Memory Address  :", id(Value))
print("Size in Bytes   :", sys.getsizeof(Value))

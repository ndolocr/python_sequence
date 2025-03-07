# Definition - A list is a sequence of items enclosed in square brackets and separated by commas.

number_line_1 = [1,2,3,4,5,6,7,8,9,10]

# List Iteration
for num in number_line_1:
    print(num)
# Enumerate - 
""""
- The enumarate function is a python built in fucntion.
- In Python, you can get both the index and value of items in a list using the enumerate() function
"""
print(list(enumerate(number_line_1)))

for index, num in enumerate(number_line_1):
    print(f"{index} {num}")
# Get the first list and separate them.
input1 = input("Enter the first list separated by commas: ")
list1 = input1.split(",")

# Get the second list and separate them.
input2 = input("Enter the second list separated by commas: ")
list2 = input2.split(",")

# Filter to find similar numbers
same = list(filter(lambda x: x in list1, list2))
result = ", ".join(same)

# Print the result
print("Items in common:", result)
# Get the strings and separate them.
strings = input("Enter a list of strings separated by spaces: ").split(' ')

# Sort the list of strings.
sorted_strings = sorted(strings, key=lambda s: (len(s), s))

# Print the result.
print("Sorted list:", sorted_strings)
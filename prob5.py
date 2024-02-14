# Get the list of numbers and separate them.
original_numbers = input("Enter numbers separated by commas: ")
numbers = list(map(int, original_numbers.split(",")))

# Get the constant.
n = int(input("Enter a constant: "))

# Get the list of numbers to the power of the constant.
power_nums = list(map(lambda x: x ** n, numbers))

# Put the list back into a string.
power_nums_str = ", ".join(map(str, power_nums))

# Print the result.
print(original_numbers, "raised to the power of", n, ":", power_nums_str)
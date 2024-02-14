#Function to get the max number as the result.
def find_maximum(numbers, compare):
    maximum = numbers[0]
    for num in numbers:
        maximum = compare(maximum, num)
    return maximum

# Variable to compare and get whichever is bigger.
compare = lambda x, y: x if x > y else y

# Get the numbers as a list and separate them.
numbers_input = input("Enter a list of numbers separated by commas: ")
numbers = list(map(int, numbers_input.split(",")))

# Call the function to find the maximum number.
result = find_maximum(numbers, compare)

# Print the result.
print("Max number:", result)
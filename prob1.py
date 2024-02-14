# Get the sum of numbers.
sum_of_numbers = lambda n: sum(map(int, str(n)))

#Take input and print the result.
number = input("Enter a number: ")
print("Sum of digits:", sum_of_numbers(str(number)))
range_number = int(input("Enter range limit: "))
numbers = range(range_number + 1)
sum_range = sum(number for number in numbers)
print("Sum of numbers in range is:", sum_range)

def second_largest(numbers):
    largest = max(numbers)
    numbers.remove(largest)
    second_largest = max(numbers)
    return second_largest

list = [10, 20, 4, 45, 99]
second_largest_element = second_largest(list)
print("the second largest number is", second_largest_element)       
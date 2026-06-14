# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    return total / count


num_array = [10, 15, 20]
result = calculate_average(num_array)
print("The average is:", result)

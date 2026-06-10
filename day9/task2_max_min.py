numbers = [45,10,89,3,56,90,12]
print(f"list: {numbers}\n")

built_in_max = max(numbers)
built_in_min = min(numbers)
print("---method 1(built_in) ---")
print(f"max = {built_in_max}")
print(f"min = {built_in_min}")

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num


print("---method 2 )manual lopp)---")
print(f"max = {largest}")
print(f"min = {smallest}")

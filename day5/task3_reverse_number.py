number=input("enter a number: ")

reversed_number = number[::-1]
print("reversed (string slicing):", reversed_number)

num_val = int(number)
rev_val = 0

while num_val > 0:
    last_digit = num_val % 10
    rev_val = (rev_val * 10) + last_digit
    num_val = num_val // 10

print("reversed (mathematical):", rev_val)

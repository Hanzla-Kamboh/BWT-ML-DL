def find_max_min(numbers_list):
    max_num = max(numbers_list)
    min_num = min(numbers_list)
    return max_num, min_num

numbers = []
for _ in range(5):
    number = float(input("Enter a number: "))
    numbers.append(number)

max_num, min_num = find_max_min(numbers)
print(f"The maximum number is {max_num} and the minimum number is {min_num}.")

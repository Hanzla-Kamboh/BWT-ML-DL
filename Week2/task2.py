def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def check_even_odd():
    number = int(input("Enter an integer: "))
    if is_even(number):
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

check_even_odd()

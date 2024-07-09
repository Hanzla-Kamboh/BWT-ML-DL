# main.py
# This script demonstrates the usage of the math package

# Importing the math package
import mymath


def main():
    try:
        # Demonstrating addition
        print(f"Addition: 3 + 2 = {mymath.add(3, 2)}")

        # Demonstrating subtraction
        print(f"Subtraction: 5 - 3 = {mymath.subtract(5, 3)}")

        # Demonstrating multiplication
        print(f"Multiplication: 4 * 2 = {mymath.multiply(4, 2)}")

        # Demonstrating division
        print(f"Division: 10 / 2 = {mymath.divide(10, 2)}")

        # Demonstrating modulus
        print(f"Modulus: 10 % 3 = {mymath.modulus(10, 3)}")

        # Demonstrating exponentiation
        print(f"Exponentiation: 2 ^ 3 = {mymath.exponentiate(2, 3)}")

        # Demonstrating square root
        print(f"Square Root: sqrt(16) = {mymath.sqrt(16)}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

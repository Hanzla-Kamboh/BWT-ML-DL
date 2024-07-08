def get_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    favorite_number = input("Enter your favorite number: ")

    user_info = {
        "name": name,
        "age": age,
        "email": email,
        "favorite_number": favorite_number
    }

    if "@" in email and "." in email:
        print(f"Hello {name}, you are {age} years old, your email is {email}, and your favorite number is {favorite_number}.")
    else:
        print("Invalid email format. Please try again.")

get_user_info()

def convert_temperature(temp, scale):
    if scale == "C":
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}°C is {converted_temp}°F")
    elif scale == "F":
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}°F is {converted_temp}°C")
    else:
        print("Invalid scale. Use 'C' for Celsius and 'F' for Fahrenheit.")
    return converted_temp

temp = float(input("Enter the temperature: "))
scale = input("Enter the scale (C/F): ")
convert_temperature(temp, scale)

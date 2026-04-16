# This program converts temperatures between Fahrenheit, Celsius, and Kelvin.
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# Convert Celsius to Kelvin
kelvin = celsius + 273.15
print(f"{celsius} degrees Celsius is equal to {kelvin} Kelvin.")
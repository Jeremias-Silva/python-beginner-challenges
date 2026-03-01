# Ask for the temperature in Celsius (input returns a string)
celsius = input("Enter the temperature in Celsius: ")

# Convert the input to a float
celsius = float(celsius)

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Print the result rounded to 2 decimal places
print(f"The temperature in Fahrenheit is {fahrenheit:.2f}")
# Ask for the user's birth year (input returns a string)
birth_year = input("Enter your birth year: ")

# Convert the input to an integer
birth_year = int(birth_year)

# Define the current year
current_year = 2026

# Calculate the age
age = current_year - birth_year

# Print the result using an f-string
print(f"You are approximately {age} years old.")
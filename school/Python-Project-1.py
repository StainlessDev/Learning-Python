S = input("Enter a string: ")

# Check if 'S' is less than 50 characters
if len(S) > 50:
    print("Invalid input: String length should be less than 50 characters.")
    exit()

# Check if 'S' has any alphanumeric characters
print("alphanumeric characters:", any(char.isalnum() for char in S))

# Check if 'S' has any alphabetical characters
print("alphabetical characters:", any(char.isalpha() for char in S))

# Check if 'S' has any digits
print("any digits:", any(char.isdigit() for char in S))

# Check if 'S' has any lowercase characters
print("lowercase characters:", any(char.islower() for char in S))

# Check if 'S' has any uppercase characters
print("uppercase characters:", any(char.isupper() for char in S))
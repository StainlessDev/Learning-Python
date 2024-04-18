
# Initialize variables to store sum, maximum, and minimum grades
total = 0
maximum = float('-inf')  # Initialize with negative infinity
minimum = float('inf')   # Initialize with positive infinity

# Read five grades from the user
for i in range(5):
    grade = float(input("Enter grade {}: ".format(i + 1)))
        
    # Update total
    total += grade
        
    # Update maximum and minimum
    if grade > maximum:
        maximum = grade
    if grade < minimum:
        minimum = grade

# Calculate average
average = total / 5

# Print statistics
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)


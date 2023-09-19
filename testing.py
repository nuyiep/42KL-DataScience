# Input string with a comma as delimiter
input_string = "apple,banana,cherry"

# Split the string using a comma as the delimiter
fruit_list = input_string.split(',')

# Initialize an empty list to store the character counts
char_counts = []

# Iterate through the elements of the fruit_list
for fruit in fruit_list:
    char_count = len(fruit)
    char_counts.append(char_count)

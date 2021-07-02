user_hex = input('Enter your hexadecimal code(without #): ').strip().upper()
# .strip removes any whitespace from user input
# .upper converts any lowercase input to uppercase

# Slices user input 3 times to get the pairs of the hexadecimal code
hex_one = user_hex[0:2]
hex_two = user_hex[2:4]
hex_three = user_hex[-2:]

# Calculates the decimal value of each sliced string in base 16.
first_converted = int(hex_one, 16)
second_converted = int(hex_two, 16)
third_converted = int(hex_three, 16)

# Prints the decimal values in rgb format
print("rgb = (", first_converted, ",", second_converted, ",", third_converted, ")")




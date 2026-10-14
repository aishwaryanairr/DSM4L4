# python
# Binary to Decimal Converter

def binary_to_decimal(binary):
    decimal = 0
    power = 0

    # Process binary digits from right to left
    for digit in reversed(binary):
        decimal += int(digit) * (2 ** power)
        power += 1

    return decimal


print("================================")
print("   BINARY TO DECIMAL CONVERTER")
print("================================")

binary = input("Enter a binary number (0s and 1s): ")

# Validate the input
if binary != "" and all(digit in "01" for digit in binary):

    decimal = binary_to_decimal(binary)

    print("Binary number:", binary)
    print("Decimal number:", decimal)

else:
    print("Invalid input! Please enter only 0s and 1s.")
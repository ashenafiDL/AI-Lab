#  Write a Python Program to Convert Roman Numbers to Decimals?

roman_numerals = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}

def roman_to_decimal(roman):
    total = 0
    i = 0
    while i < len(roman):
        if i < len(roman)-1 and roman[i:i+2] in roman_numerals:
            total += roman_numerals[roman[i:i+2]]
            i += 2
        else:
            total += roman_numerals[roman[i]]
            i += 1
    return total

# use this as an example "XIV"
roman_num = input("Enter a roman numeral: ")
decimal_num = roman_to_decimal(roman_num)
print(f"The decimal equivalent of {roman_num} is {decimal_num}")


# Author: Matthew Stefanovic
# 
# This program takes user input for a number, its original base, 
# and the base to convert it to. It then validates the input and
# converts the number to the desired base. The program raises custom
# exceptions for invalid inputs. The digits used for the number 
# system are stored in a string. The program will continue to 
# prompt the user for input until valid inputs are entered. 
# Once valid inputs are entered, the program prints the converted number 
# to the console.


class InvalidNumberError(Exception):
    pass

class NumberGreaterThanBase(Exception):
    pass

def convert_base(number, original_base, new_base):
    decimal = 0

    if original_base == new_base:
        return number
    
    # Convert input number to decimal
    for i, digit in enumerate(number[::-1]):
        decimal += digits.index(digit) * (original_base ** i)
    
    # Convert decimal to output base
    output = ""
    while decimal > 0:
        digit = decimal % new_base
        output = digits[digit] + output
        decimal //= new_base
    
    return output


digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    try:
        number = input('==> Please enter the first number: ').upper()
        if number == '':
            raise ValueError()

        original_base = int(input('==> Please enter the base for that number: '))
        if original_base <= 0:
           raise InvalidNumberError('Base must be greater than zero')

        new_base = int(input('==> Please enter the original_base you want to convert to: '))
        if new_base <= 0:
           raise InvalidNumberError('Base must be greater than zero')

        for digit in number:
            if digit not in digits:
                raise NumberGreaterThanBase(f'The digit {digit} is not a valid digit')

            if digits.index(digit) >= original_base:
                raise NumberGreaterThanBase(f'The digit {digit} is greater than base {original_base} allows')

        break
    except ValueError:
        print('Please enter a valid number')
    except InvalidNumberError as e:
        print(e)
    except NumberGreaterThanBase as e:
        print(e)
    except KeyboardInterrupt:
        print()
        print()
        print('Now Exiting :)')
        exit(0)
    except: 
        print('Unknown error occurred, please try again')


    print()

answer = convert_base(number, original_base, new_base)

print(answer)

def convert_base(number, base1, base2):
    if base1 == base2:
        return number

    if base1 > base2:
        big_to_small(number, base1, base2)

    if base1 < base2:
        small_to_big(number, base1, base2)

def big_to_small(number, base1, base2):
    

def small_to_big(number, base1, base2):
    pass 

class InvalidNumberError(Exception):
    pass

class NumberGreaterThanBase(Exception):
    pass

while True:
    try:
        number = float(input('==> Please enter the first number: '))
        if number >= base1:
            raise NumberGreaterThanBase('Your number can\'t be greater than the base')

        base1 = int(input('==> Please enter the base for that number: '))
        if base1 <= 0:
           raise InvalidNumberError('Base must be greater than zero')

        base2 = int(input('==> Please enter the base for that number: '))
        if base2 <= 0:
           raise InvalidNumberError('Base must be greater than zero')

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

answer = convert_base(number, base1, base2)

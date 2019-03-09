
def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """
    numbers = []

    def palindrome (some_number):
            """ check if a number is a palindrome """
            some_number = str(some_number)
            if some_number[::-1] == some_number:
                return True
            else:
                return False
        

    for number in range (100000,1000000):
        if palindrome(str(number)[2:]) == True:
            if palindrome(str(number+1)[1:]) == True:
                if palindrome(str(number+2)[1:5]) == True:
                    if palindrome (number+3) == True:
                        # print (number)
                        numbers.append(number)
        if number == 999999:

            return numbers




if __name__ == '__main__':
    # Question 2
    return_value = check_palindrome()

    print(f"Question 2 solution: {return_value}")
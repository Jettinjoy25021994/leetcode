"""
Checks the given number is palindrome or not

Solution Approach
-----------------
Reverse the number till half, if the first half is equal to the second half
then its a palindrome number
"""

def is_palindrome_number(number : int) -> bool:
    """
    Checks the given number is palindrome or not
    returns true if palindrome else false
    Parameters
    ----------
    number: number to be checked

    Returns
    -------
    is_palindrome: boolean value indicating whether the given number
                   is palindrome or not
    """
    rev = 0
    while number > rev:
        # we can exit the loop if the reversed half is greater non reversed half
        rev = (rev * 10) + (number % 10)
        number = number // 10
    
    is_palindrome = number == rev or number // 10 == rev # handle edge case for odd length
    return is_palindrome

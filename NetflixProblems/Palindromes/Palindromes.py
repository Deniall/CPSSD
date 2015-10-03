def iterativePalindrome():

    palindrome = raw_input().lower() # .lower() makes it case insensitive

    length = len(palindrome)

    i = 0

    while i < length / 2 + 1:
        if palindrome[i] != palindrome[-i - 1]:
            return False # iterates until it finds a case where two corresponding letters are not the same

        i += 1

    else:
        return True


def recursivePalindrome(palindrome):

    palindrome.lower() # makes the function case insensitive

    if len(palindrome) < 2:
        return True # the base case
    if palindrome[0] != palindrome[-1]:
        return False #this means the first and last letters are different, hence not a palindrome

    return recursivePalindrome(palindrome[1:-1]) # the recursive step
        
            

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

def anagramPalindrome():
    from itertools import permutations # this module finds all permuations of a string
    string = raw_input().lower()
    anagrams = [''.join(chars) for chars in permutations(string)] # creates a set of the permuations(anagranms)
    i = 0
    k = 0
    while i <= len(set(anagrams)): # the earlier iterative function to check palindromes(badly implemented)
        palindrome = anagrams[i] 
        length = len(palindrome)
        while k < length / 2 + 1:
            if palindrome[k] != palindrome[-k - 1]:
                return "False" 

                k += 1
            else:
                return "True"
        i+=1
    

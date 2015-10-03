def palindromeIterative(i=0):
    if i == 0:
        print "This is the iterative version of the program that checks if a string is a palindrome. To break out of the function, type 'exit'."
    palindrome = raw_input().lower()
    first_half = palindrome[:len(palindrome)//2]
    second_half = palindrome[len(palindrome)//2:]
    if len(palindrome)%2 != 0:
        first_half = palindrome[:len(palindrome)//2+1]
    if palindrome == "exit":
        a = 1 / 0  # will raise an exception, this is to break out of the function
        return a
    if second_half[::-1] == first_half:
        print "True"
        palindromeIterative(i+1)
    else:
        print "False"
        palindromeIterative(i+1)

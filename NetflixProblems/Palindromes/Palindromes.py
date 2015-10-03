def iterativePalindrome():
    palindrome = raw_input().lower()
    length = len(palindrome)
    i = 0
    while i < length / 2 + 1:
        if palindrome[i] != palindrome[-i - 1]:
            print "F"
            iterativePalindrome()
        i += 1
    else:
        print "T"
        iterativePalindrome()

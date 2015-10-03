palindrome = raw_input()
first_half, second_half = palindrome[:len(palindrome)//2], palindrome[len(palindrome)//2:]
if second_half[::-1] == first_half:
    print "True"
else:
    print "False"

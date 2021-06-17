def palindrome(st):
    rev=st[::-1]
    if rev==st:
        return True
    else:
        return False
a=input('Enter a word to check palindrome:')
ans=palindrome(a)
if ans==True:
    print(a,'is a palindrome string')
else:
    print(a,'is not palindrome string')

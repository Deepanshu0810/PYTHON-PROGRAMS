def check(i):
    num1,num2=i,i
    result=0
    rev=0
    n=len(str(i))
    while num2:
        digit=num2%10
        rev=rev*10+digit
        num2=num2//10
        
    while(num1!=0):
        digit=num1%10
        result+=digit**n
        num1=num1//10
        
    if result==i and rev==i:
        print(i,'is ARMSTRONG NUMBER as well as PALINDROME')
    elif rev==i and result!=i:
        print(i,'is not ARMSTRONG NUMBER but PALINDROME')
    elif result==i and rev!=i:
        print(i,'is ARMSTRONG NUMBER but not PALINDROME')
    else:
        print(i,'is neither ARMSTRONG NUMBER nor PALINDROME')
a=int(input('Enter a positive number:'))
check(a)

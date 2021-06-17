def factorial(x):
    fact=1
    if x==0:
        return 1
    for i in range(x,0,-1):
        fact*=i
    return fact
n=int(input('Enter num to calculate factorial:'))
print('The factorial of',n,'is:',factorial(n))

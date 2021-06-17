def prime(x):
    if x==0 or x==1:
        print('Neither Prime Nor Composite')
    else:
        for i in range(2,x):
            if x%i==0:
                print('Number',x,'is a composite number')
                break
        else:
            print(x,'is a prime number')
            
n=int(input('Enter a number:'))
prime(n)

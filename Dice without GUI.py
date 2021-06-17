import random
while True:
    print('Press the "Enter" key to roll a dice or "q" to quit')
    ch=input()
    if ch=='':
        n=random.randint(1,6)
        print('You got the number',n)
    elif ch=='q' or ch=='Q':
        print('Thank You for playing')
        break
    else:
        print('Please press a valid key')
        

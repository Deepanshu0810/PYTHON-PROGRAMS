#----linear searching---#
def search(ar,item):
    i=0
    while i<len(ar) and ar[i]!=item:
        i=i+1
    if i<len(ar):
        return i
    else:
        return False

#__main__#
N=int(input('Enter no of elements required:'))
Ar=[0]*N
for a in range(N):
    Ar[a]=int(input('Enter element:'))
print('Your list is :')
print(Ar)
sitem=int(input('Enter element to search for:'))
res=search(Ar,sitem)
if res==False:
    print('Element not found')
else:
    print('Element found at index',res)

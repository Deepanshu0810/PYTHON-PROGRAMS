#----binary search----
def search(ar,item):    
    beg=0
    last=len(ar)-1
    while beg<=last:
        mid=int((beg+last)/2)
        if item==ar[mid]:
            return mid
        elif item<ar[mid]:
            last=mid-1
        elif item>ar[mid]:
            beg=mid+1
    else:
        return False

##################__main__#####################
N=int(input('Enter no of elements to be entered:'))
Ar=[0]*N
for a in range(N):
    Ar[a]=int(input('Enter Element:'))
print(Ar)
sitem=int(input('Enter element to search for:'))
res=search(Ar,sitem)
if res==False:
    print('Not found')
else:
    print('Element found at index',res)


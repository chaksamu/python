pos=-1
def search(list,s):
    l=0
    u=len(list)-1
    print(l,u)
    while l<=u:
        mid=(l+u) // 2
        print(mid)
        if list[mid]==s:
            globals()['pos']=mid
            return True
        else:
            if list[mid] < s:
                l=mid+1
            else:
                u=mid-1
    return False


list=[1,2,3,4,5,6,7,8,9,10,11]
s=11
if search(list,s):
    print("Found",pos)
else:
    print("NotFound")
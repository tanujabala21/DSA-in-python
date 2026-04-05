#check if array is sorted or not
def issorted(n):
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
           return False
    return True

print(issorted([2,1,3,4,5]))
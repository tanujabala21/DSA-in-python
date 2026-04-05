#remove the duplicates in the array
def removeduplicates(arr):
    slow=0
    for fast in range(1,len(arr)):
        if arr[fast]!=arr[slow]:
            slow+=1
            arr[slow]=arr[fast]
    return arr[:slow+1]

print(removeduplicates([2,2,2,2,3,4,4,6]))
        
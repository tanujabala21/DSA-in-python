#selection sorting

#At every step, find the smallest element from 
# the remaining unsorted part and put it in its correct position.


n=[5,3,4,2,1]
for i in range(len(n)):
    min_index=i
    for j in range(i+1,len(n)):
        if n[j]<n[min_index]:
            min_index=j
        
    n[i],n[min_index]=n[min_index],n[i]

print(n)
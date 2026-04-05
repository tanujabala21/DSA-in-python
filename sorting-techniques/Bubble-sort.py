#Bubble sort

#Compare two neighboring elements. If the left one is bigger, swap them.
 
n=[5,4,3,2,1]
for i in range(len(n)):
    for j in range(len(n)-1-i):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(n)
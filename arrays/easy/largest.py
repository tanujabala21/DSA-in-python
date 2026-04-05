#largest in arry
n=[3,2,1,4,6]
large=n[0]
for i in range(1,len(n)):
    if n[i]>large:
        large=n[i]
print(large)
#second largset element in array
n=[10,10,10,10]
first=n[0]
sec=0
for i in range(len(n)):
    if n[i]>first:
        sec=first
        first=n[i]
    elif n[i]>sec and n[i]!=first:
        sec=n[i]

print(sec)




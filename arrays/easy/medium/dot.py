n=[-7,-3,-2,3,5,1]
left=0
right=len(n)-1
while left<right:
    left_square=n[left]**2
    right_square=n[right]**2

    if left_square>right_square:
        left_square,right_square=right_square,left_square
        left+=1
        right-=1
    else:
        left+=1
        right-=1
    print(n)


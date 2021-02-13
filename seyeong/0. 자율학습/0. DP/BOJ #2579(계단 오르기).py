
def stair(n):
    one_step = [0]
    two_step = [0]

    for i in range(1, n+1):
        p = int(input())
        if i <= 2:
            one_step.append(p+one_step[i-1])
            two_step.append(p)
        else:
            one_step.append(two_step[i-1]+p)
            two_step.append(max(one_step[i-2], two_step[i-2])+p)
            
        
    return max(one_step[-1], two_step[-1])

print(stair(int(input())))
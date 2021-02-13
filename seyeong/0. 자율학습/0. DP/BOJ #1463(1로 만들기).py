
def to_one(n):
    arr = [0]
    
    for i in range(1, n+1):
        values = []
        if i == 1:
            arr.append(0)
            
        else:
            if i % 2 == 0:
                values.append(arr[i//2] + 1)
            
            if i % 3 == 0:
                values.append(arr[i//3] + 1)
        
            values.append(arr[i-1] + 1)

            arr.append(min(values))
            
    return arr[-1]

print(to_one(int(input())))
    
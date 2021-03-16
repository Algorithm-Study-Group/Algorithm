import math

r, c, k = map(int, input().split())

# graph = []

# for i in range(r):
#     row = []
#     for j in range(1,c+1):
#         row.append(c*i+j)
    
#     graph.append(row)

# print(target_row, target_col)

# print(math.factorial(0))
# print(graph)


def count_path(k):

    if k == 0:
        return int(math.factorial(r+c-2) / math.factorial(r-1) / math.factorial(c-1))

    else:
        t1, t2 = (k-1)//c, (k-1)%c
        result_1 = math.factorial(t1+t2) / math.factorial(t1) / math.factorial(t2)
        result_1 = int(result_1)
        if t1 == r-1 or t2 == c-1:
            result_2 = 1
        else:
            e1, e2 = (r-1-t1), (c-1-t2)
            result_2 = math.factorial(e1+e2) / math.factorial(e1) / math.factorial(e2)      
            result_2 = int(result_2)
        return result_1 * result_2
print(count_path(k))



import sys, collections
t = int(sys.stdin.readline().strip())


for _ in range(t):
    tel_list = collections.defaultdict(list)
    ans = 0
    n = int(sys.stdin.readline().strip())

    for i in range(n):
        tel = sys.stdin.readline().strip()
        
        for num in tel_list[tel[0]]:
            l = min(len(tel), len(num))
            # print([num[:l], tel[:l], l])
            if num[:l] == tel[:l]:
                ans = 1
                break
        
        if ans == 1:
            print("NO")
            break

        tel_list[tel[0]].append(tel)
        # print(tel_list)
    if not ans:
        print("YES")
        
        
            
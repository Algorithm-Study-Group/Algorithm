import sys, collections
s = sys.stdin.readline().strip()
counter = collections.Counter(s)
l = len(counter)

size = len(s)-l
# print(counter.most_common())
# print(size)
# answer = size
# counter = collections.Counter()
answer = False
# print(s.count("ab"))
while True:
    if l == 1:
        print(len(s)-1)
        break

    substring = {}
    
    left, right = 0, size
    for i in range(len(s)-size+1):
        if substring.get(s[left+i:right+i]) is None:
            substring[s[left+i:right+i]] = 1
        else:
            print(size)
            answer = True
            break
    if answer:
        break
    size -= 1
    

        # substring.append(s[left+i:right+i])
        # counter = collections.Counter(substring)
    
    # if max(substring.values()) > 1:
        
    #     print(size)
    #     break
    # else:
    #     size -= 1
    

# print(max(substring.values()))

# # print(substring)
# print(counter.most_common(1)[0][1])
import sys, collections
t = int(sys.stdin.readline().strip())

class Node:
    def __init__(self, c):
        self.val = c
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def add(self, word):
        cur = self.head
        
        for char in word:
            if cur.end:
                return False
            elif cur.children.get(char) is None:
                cur.children[char] = Node(char)
            cur = cur.children[char]
        
        if len(cur.children) > 0:
            return False
        else:
            cur.end = True
            return True
            # if cur:
            #     return False
        # cur['end'] = True
    

    # def startWith(self, word):
    #     cur = self.head

    #     for ch in word:
    #         if ch not in cur:
    #             return False
    #         cur = cur[ch]
    #         # print(len(cur))
    #     return True if len(cur) > 0 else False



for _ in range(t):

    tel_list = Trie()
    
    answer = True
    n = int(sys.stdin.readline().strip())

    for i in range(n):
        tel = sys.stdin.readline().strip()
        if answer:
            if not tel_list.add(tel):
                answer = False
        else:
            pass
        
    if answer:
        print("YES")
    else:
        print("NO")
        
    
    # # print(sorted(answer, key=lambda x: len(x)))
    # answer = sorted(answer, key=lambda x: len(x))
    # # print(answer)
    # for num in answer:
    #     if tel_list.startWith(num):
            
    #         # print(ans)
    #         print("NO")
    #         ans = 1
    #         break
    # if ans == 0:
    #     print("YES")
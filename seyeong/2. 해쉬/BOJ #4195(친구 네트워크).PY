import collections
class unionFind():
    
    def __init__(self):
        self.data = collections.defaultdict(list)
        
    def add(self, idx, str):
        self.data[idx].append(str) 


    def find(self, name):
        for key, value in self.data.items():
            
            if name in value:
                return key 
       
    def union(self, name1, name2, idx):

        a, b = self.find(name1), self.find(name2)
        
        if a == b:
            # print(self.data)
            return

        else:
            self.data[a] += self.data[b]
            self.data[a] = list(set(self.data[a]))
            self.data.pop(b)
            if self.data[i]:
                self.data.pop(i)
            # print(self.data)
            return 
    
    def length(self, name):
        idx = self.find(name)
        return len(self.data[idx])

n_test = int(input())

for _ in range(n_test):
    n_rel = int(input())
    u = unionFind()
    for i in range(n_rel):
        p1, p2 = input().split()
        u.add(i, p1)
        u.add(i, p2)
        u.union(p1, p2, i)
        print(u.length(p1))



# test = unionFind()

# test.add(3, "abcd")
# test.add(1, "cdef")

# print(test.find("abcd"))

# test.union("abcd", "cdef")

# print(test.find("cdef"))

# test.add(3, "fedd")

# print(test.find("fedd"))

# print(test.length("fedd"))




import sys, collections

n = int(sys.stdin.readline().strip())

entry = []
out = []
answer = 0

for i in range(n):
    name = sys.stdin.readline().strip()
    entry.append(name)

while entry:
    name = sys.stdin.readline().strip()
    out = entry[0]
    if out == name:
        entry.remove(name)
    else:
        answer += 1
        entry.remove(name)
    
    
print(answer)


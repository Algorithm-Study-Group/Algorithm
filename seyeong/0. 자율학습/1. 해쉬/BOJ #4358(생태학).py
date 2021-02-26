import sys, collections

cnt = 0
dict = collections.defaultdict(int)

while True:
    name = sys.stdin.readline().strip()
    if not name:
        break
    cnt += 1
    dict[name] += 1

for key, value in sorted(dict.items(), key=lambda x:x[0]):
    print(key, f'{(value/cnt*100):0.4f}')
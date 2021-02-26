import collections

n = int(input())

nums = list(map(int, input().split()))

counter = collections.Counter(nums)

# print(counter)

m = int(input())

targets = list(map(int, input().split()))

answer = []
for target in targets:
    answer.append(str(counter[target]))


ans = ' '.join(answer)
print(ans)
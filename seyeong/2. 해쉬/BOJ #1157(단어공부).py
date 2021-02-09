import collections

s = input().upper()

c = collections.Counter(s)

# print(c.most_common(1))
# print(len(c))
if len(c) >= 2:
    a,b = c.most_common(2)

    print(a[0] if a[1] != b[1] else "?")

else:
    print(c.most_common()[0][0])
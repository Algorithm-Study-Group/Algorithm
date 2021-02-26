import collections

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

dic = collections.defaultdict(list)

for inf in info:
    a,b,c,d,e = inf.split(" ")
    dic[e].append([a,b,c,d])

# print(dic)

for i in range(len(query)):
    
    a, _, b, _, c, _, d, e = query[i].split(" ")
    query[i] = [a,b,c,d,e]

# print(query)

for q in query:
    score = q[-1]
    
    for k, v in dic.items():
        if int(k) >= int(score):
            print(k,v)
            # pass

s = input()

def search_pattern(pattern):

    pi = [0] * len(pattern)
    # print(pi)
    j = 0


    # while i < len(pattern):
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        
        # 검사 시 일치하는 접두사/접미사 있으면 다음 검사
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    
    return max(pi)
    
ans = 0    
for i in range(len(s)):
    ans = max(ans, search_pattern(s[i:]))
print(ans)
import sys

s = sys.stdin.readline().strip()

# print(s)
buffer = ''
answer = ''
sw = 0

for char in s:
    if char == '>':
        sw = 0
        buffer += char
        answer += buffer 
        buffer = ''
        continue


    if char == '<':
        answer += buffer[::-1]
        buffer = ''
        sw = 1
    
    if char == ' ' and sw == 0:
        answer += buffer[::-1]
        answer += ' '
        buffer = ''
        continue

        
    
    buffer += char
answer += buffer[::-1]
    
print(answer)

    
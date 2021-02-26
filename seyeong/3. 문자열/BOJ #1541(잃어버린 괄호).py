
s = input()
answer = ''
sw = 0

for char in s:

    
    if char =='-' and sw == 1:
        sw = 0
        answer += ')'
        
        

    if char == '-' and sw == 0:
        sw = 1
        answer += char
        answer += '('
        continue

    
    else:
        if not answer or answer[-1] in '+-(':
            if char == '0':
                continue
        answer += char

if sw == 1:
    answer += ')'
# print(answer)
print(eval(answer))


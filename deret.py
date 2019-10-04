deret = ''
n = 3
cond = 3
for i in range(1, 1001):
    if i == cond:
        deret += f'* {i} '
        cond = i + n
        n = 2 if n == 3 else 3
    else:
        deret += f'{i} '

print(deret) 
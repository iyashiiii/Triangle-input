ij = 0
l = []
while ij<4:
    x = input()
    for i in x:
        if i == ' ' or '':
            l.append(0)
        l.append(int(i))
    ij+=1

print(l)

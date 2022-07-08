
f1 = open('25.xyz', 'r')
f2 = open('trash.txt', 'w')
first = True
i = 9
for line in f1:
    if(line[0] == '4'):
        i += 1
        f2.close()
        f2 = open(str(i) + '0.txt', 'w')
    if(line[0] == '='):
        f2.close()
        f2 = open('trash.txt', 'w')
    if(line[0] == '1'):
        f2.write('10' + line[1:])
    elif(line[0] == '3'):
        f2.write('100' + line[1:])
    else:
        f2.write(line)

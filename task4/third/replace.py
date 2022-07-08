
for i in range(10,26):
    f1 = open(str(i)+'.xyz', 'r')
    f2 = open(str(i)+'0.txt', 'w')
    for line in f1:
        if(line[0] == '1'):
            f2.write('10' + line[1:])
        elif(line[0] == '3'):
            f2.write('100' + line[1:])
        else:
            f2.write(line)


dic = {}
with open(r"C:\Users\Slam\Documents\dataset_3380_5.txt") as inf:
    for line in inf:
        line = line.lower().strip().split()
        #print(line)
        if line[0] not in dic:
            dic[line[0]] = [0, 0]
            dic[line[0]][1] += int(line[2])
            dic[line[0]][0] += 1
        else:
            dic[line[0]][1] += int(line[2])
            dic[line[0]][0] += 1
for i in range(1, 12):
    if str(i) not in dic:
        print(i, '-')
    else:
        print(i, int(dic[str(i)][1]) / int(dic[str(i)][0]))
#print(dic)

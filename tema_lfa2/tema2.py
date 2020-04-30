def union2(test_dict1,test_dict2):
    res = {key: list(set(test_dict1.get(key, []) + test_dict2.get(key, [])))
           for key in set(test_dict2) | set(test_dict1)}
    return res

f=open("date.txt")
n=int(f.readline())
s_fin=[x for x in f.readline().split()]
limbaj=[x for x in f.readline().split()]

dict={}
lines=f.readlines()
for line in lines:
    init, leg, fin = [x for x in line.split()]
    if init not in dict.keys():
        dict[init]={}
    if leg not in dict[init].keys():
        dict[init][leg]={}
    dict[init][leg]=fin

#print(dict)

d={}
for i in dict.keys():
    for j in dict.keys():
        if i>j:
            if i not in d.keys():
                d[i]={}
            d[i][j]={}

for i in d.keys():
    if i in s_fin:
        for j in d[i].keys():
            if j not in s_fin:
                d[i][j]='#'
    if i not in s_fin:
        for j in d[i].keys():
            if j in s_fin:
                d[i][j]='#'
#print(d)

ok=1
while ok==1:
    ok=0
    for i in d.keys():
        for j in d[i].keys():
            if d[i][j]=={}:
                for k in limbaj:
                    if k in dict[i].keys() and k in dict[j].keys():
                        if dict[i][k]>dict[j][k]:
                            if d[dict[i][k]][dict[j][k]]!={}:
                                d[i][j]='#'
                                ok=1
                        elif dict[i][k]<dict[j][k]:
                            if d[dict[j][k]][dict[i][k]]!={}:
                                d[i][j]='#'
                                ok=1

#print(d)

for i in dict.keys():
    for j in dict[i].keys():
        dict[i][j]=list(dict[i][j])

for i in d.keys():
    for j in d[i].keys():
        if d[i][j]=={}:
            dict[i]=union2(dict[i],dict[j])
            dict[j+i]=dict[i]
            for k in dict.keys():
                for l in dict[k].keys():
                    if dict[k][l]==i or dict[k][l]==j:
                        dict[k][l]=j+i
            for k in d.keys():
                if k>i:
                    if d[k][j]=='#':
                        d[k][j+i]='#'
                    if d[k][j]=={}:
                        d[k][j+i]={}
                    del d[k][i]
                    del d[k][j]

            del dict[i]
            del dict[j]
            #print(dict)

for i in dict.keys():
    for j in dict[i].keys():
        if len(dict[i][j])>1:
            dict[i][j].sort()
            s="".join(dict[i][j])
            dict[i][j]=s
        elif dict[i][j][0] in i:
            dict[i][j]=[i]
print(dict)



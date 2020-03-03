f = open("date.txt")

cuvant = f.readline()
n, s_init = [x for x in f.readline().split()]
st_fin = [x for x in f.readline().split()]
# print(st_fin)
a = [['#' for _ in range(int(n))] for x in range(int(n))]


lines = f.readlines()
for line in lines:
    init, leg, fin = [x for x in line.split()]
    if init.isdigit() == True:
        if a[int(init)][int(fin)] == '#':
            a[int(init)][int(fin)] = [leg]
        else:
            a[int(init)][int(fin)].append(leg)
    else:
        if a[ord(init)-ord('a')][ord(fin)-ord('a')] == '#':
            a[ord(init) - ord('a')][ord(fin) - ord('a')] = [leg]
        else:
            a[ord(init) - ord('a')][ord(fin) - ord('a')].append(leg)
print(a)

poz = 0
ok = 1
for i in range(len(cuvant) - 1):
    for j in range(int(n)):
        if cuvant[i] in a[poz][j]:
            poz = j
            #print(poz)
            break
    else:
        ok = 0
# print(poz)

if ok == 1:
    if str(poz) in st_fin:
        print("DA")
    else:
        print("Nu ajunge in stare finala")
else:
    print("Cuvant gresit")
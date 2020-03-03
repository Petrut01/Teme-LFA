f = open("date.txt")

cuvant = f.readline()
n, s_init = [x for x in f.readline().split()]
st_fin = [x for x in f.readline().split()]
# print(st_fin)
a = [['#' for _ in range(int(n))] for x in range(int(n))]

if s_init.isdigit():
    s_init = int(s_init)
else:
    s_init = ord(s_init) - ord('a')

lines = f.readlines()
ok1 = 1
for line in lines:
    init, leg, fin = [x for x in line.split()]
    if init.isdigit() == True:
        if a[int(init)][int(fin)] == '#':
            a[int(init)][int(fin)] = [leg]
        else:
            a[int(init)][int(fin)].append(leg)
    else:
        if a[ord(init) - ord('a')][ord(fin) - ord('a')] == '#':
            a[ord(init) - ord('a')][ord(fin) - ord('a')] = [leg]
        else:
            a[ord(init) - ord('a')][ord(fin) - ord('a')].append(leg)
        ok1 = 0
print(a)

poz = s_init
ok = 1

for i in range(len(cuvant) - 1):
    for j in range(s_init, int(n)):
        if cuvant[i] in a[poz][j]:
            poz = j
            # print(poz)
            break
    else:
        ok = 0
# print(poz)
if ok1 == 0:
    poz = chr(ord('a') + poz)
if ok == 1:
    if str(poz) in st_fin:
        print("DA")
    else:
        print("Nu ajunge in stare finala")
else:
    print("Cuvant gresit")

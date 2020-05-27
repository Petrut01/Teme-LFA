f=open("date.txt",'r')
n=int(f.readline())
neterm=[x for x in f.readline().split()]
term=[x for x in f.readline().split()]
start=f.readline().strip()
dict = {}

for i in f.readlines():
    a,b=[ x for x in i.split()]
    dict[a]=[x for x in b.split('|')]

print(dict)

def nr_term(x):
    nr = 0
    for i in x:
        if i in term:
            nr += 1
    return nr

def nr_neterm(x):
    nr = 0
    for i in x:
        if i in neterm:
            nr += 1
    return nr

def generare(l,x):
    for cuv in l:
        aux = x.replace('*', cuv)
        if nr_term(aux) <= n :
            #print(aux)
            if nr_neterm(aux):
                for i in aux:
                    if i in neterm:
                        ntm = i
                        aux = aux.replace(i, '*',1)
                        #print(aux)
                        break
                generare(dict[ntm],aux)
            else:
                if len(aux) > 1:
                    aux = aux.replace('#','')
                cuvinte.add(aux)

cuvinte = set()
try:
    generare(dict[start],'*')
    if n == 0:
        print("Dimensiune invalida")
    else:
        for cuv in sorted(cuvinte):
            print(cuv)
except KeyError:
    print("GIC gresita")

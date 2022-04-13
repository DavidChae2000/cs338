


p = 59
g = 11
a = 57
b = 44
alist = []
blist = []

for x in range(p):
    if g**x % p == a:
        alist.append(x)

for x in range(p):
    if g**x % p == b:
        blist.append(x)

if len(alist) == 1 and len(blist) == 1:
    print('K = ' + str(b**alist[0]%p))
else:
    check = FALSE
    for x in range(len(alist)):
        for y in range(len(blist)):
            if b**alist[x]%p == a**blist[y]%p:
                print('K = ' + str(b**alist[x]%p))
                break
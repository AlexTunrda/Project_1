from itertools import product
n = 0
for x in product('0123456789', repeat=6):
    s = ''.join(x)
    if s[-1] != '7' and s[-2]!='8' and  s[-1] != '8' and s[-2]!='7'  and len(set(i for i in s)) == len(s) and s.count('5')>0 and s.count('6')>0:
        print(s)
        n+=1
print(n)
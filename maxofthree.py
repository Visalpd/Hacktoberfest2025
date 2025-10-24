a = 10
b = 14
c = 12

res = a if (a >= b and a >= c) else (b if b >= c else c)
print(res)

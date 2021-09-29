
def factors(n):
    i = 2
    fact = []
    while i <= n:
        if (n%i) == 0:
            fact.append(i)
            n = n/i
        else:
            i = i+1
    return fact

x = int(input())
y = factors(x)


if (x**0.5) < float(max(y)):
    print('strange')
else:
    print('not')
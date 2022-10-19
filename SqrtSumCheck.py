def sqrtsumcheck(n):
    for a in range(0, n + 1):
        for b in range(0, n + 1):
            if (a + b + (2 * ((a * b)**(1/2)))) == n:
                print(a, b)
sqrtsumcheck(2023)

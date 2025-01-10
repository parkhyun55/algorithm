while True:
    n = int(input())
    l = []
    
    if n == -1:
        break
    
    for i in range(1, n):
        if n % i == 0:
            l.append(i)

    if n == sum(l):
        print(n, " = ", " + ".join(str(i) for i in l), sep="")

    else:
        print(str(n) + " is NOT perfect.")
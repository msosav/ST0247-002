def fibonacci(n):
    a = [0]*(n+1)
    a[0]=1
    a[1]=1
    for i in range(2,n+1):
        a[i] = a[i-1] + a[i-2] ## Caso recursivo con arreglos
    return a[n]

def main():
    print(fibonacci(4))
main()
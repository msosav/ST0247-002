def fibonacci(n):
    if n <= 1:
        return 1
    else:
        if n > 1:
            return fibonacci(n-1) + fibonacci(n-2)

def main():
    print(fibonacci(2))
main()
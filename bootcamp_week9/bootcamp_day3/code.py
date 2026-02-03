def fibonacci(n):
    if n <= 1: # Base case
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

if __name__ == '__main__':
    with open('code.py', 'w') as f:
        f.write(str(fibonacci))
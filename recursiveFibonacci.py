# recursively return nth fibonacci number

def recursiveFibonacci(n):
    if n <= 1:
        return n
    return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)

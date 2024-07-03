# return nth fibonacci number iteratively

def fibonacci(n):
    if n < 2:
        return 1
    fibList = [1,1]
    for i in range(2, n):
        fibList.append(fibList[i-2] + fibList[i-1])
    return fibList[-1]

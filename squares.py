# generate first n squares

def square(n):
  squareList = []
  for i in range(1, n+1):
    squareList.append(i^2)
  return squareList

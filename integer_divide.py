# Given two integers: x and y; return x ÷ y without using / (division) or * (multiplication) operators.
# Note: Assume that both integers are positive.

def integer_divide(x, y):
  temp = y
  result = 1
  if x < y:
    return 0
  
  while (x-temp) > temp:
    temp <<= 1
    result <<= 1
  
  return ((result)+integer_divide((x-temp),y))

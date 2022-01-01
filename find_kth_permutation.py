def factorial(n):
  if n==1:
    return 1
  else:
    return n*factorial(n-1)

def find_kth_permutation(v, k, result):
  v_len = len(v)
  i = 0
  perms = factorial(v_len)
  print ("for the vector {} there will be {} permutations".format(v,perms))
  while v_len > 0 :
    result += str(v[((k-1)//(perms//v_len))])
    print (v[((k-1)//(perms//v_len))])
    del(v[((k-1)//(perms//v_len))])
    k = (k-1) % (perms // v_len)
    perms = perms // v_len
    v_len -= 1
  print(result)

  return 

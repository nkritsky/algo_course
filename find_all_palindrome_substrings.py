def check_for_longer_even_palindrome(input, i, size, i_len):
  # input - string where we look for p
  # i - where the current palindrome originated (the seed)
  # size - size of the current palindrome
  # i_len - length of input string
  if i-size < 0 or i+1+size > i_len-1:
    return 0
  elif input[i-size] != input [i+1+size]:
    return 0
  else:
    return 1+check_for_longer_even_palindrome(input,i,size+1,i_len)

def check_for_longer_odd_palindrome(input, i, size, i_len):
  # input - string where we look for p
  # i - where the current palindrome originated (the seed)
  # size - size of the current palindrome
  # i_len - length of input string
  if i-size < 0 or i+2+size > i_len-1:
    return 0
  elif input[i-size] != input [i+2+size]:
    return 0
  else:
    return 1+check_for_longer_odd_palindrome(input,i,size+1,i_len)

def find_all_palindrome_substrings(input):
  # find all 2-letter palindromes
  # for each 2-letter p, check the letters before and after to see if the bigger one is 
  # the p-drome too, do recursion
  # find all 3 letter p
  # also recursively check for longer p's
  p_count = 0
  i_len = len(input)
  for i in range(i_len-1):
    if input[i] == input [i+1]:
      p_count = p_count + 1 + check_for_longer_even_palindrome(input,i,1,i_len)
      if i < i_len-2:
        if input[i] == input[i+2]:
          p_count = p_count + 1 + check_for_longer_odd_palindrome(input,i,1,i_len)
  return p_count

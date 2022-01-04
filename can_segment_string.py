def can_segment_string_by_index(s,dictionary,i):
  for word in dictionary:
    j = i
    is_match = True
    for c in word:
      if c != s[j]:
        is_match = False
        break
      j+=1
    if is_match:
      return True
      if can_segment_string_by_index(s,dictionary,j):
        return True
  return False


def can_segment_string(s, dictionary):
  for word in dictionary:
    i = 0
    is_match = True
    for c in word:
      if c != s[i]:
        is_match = False
        break
      i+=1
    if is_match == True:
      if can_segment_string_by_index(s,dictionary,i):
        return True
  return False

def remove_white_spaces (s):
  read_p = 0
  write_p = 0
  for c in s:
    if s[read_p] != ' ' and s[read_p] != '\t':
      s[write_p] = s[read_p]
      write_p += 1
    read_p +=1
  s[write_p]='\0'
  return s

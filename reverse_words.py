# Reverse the order of words in a given sentence (an array of characters). 

def reverse_chars(sentence, start, end):
  temp = ''
  while start < end:
    temp=sentence[start]
    sentence[start]=sentence[end]
    sentence[end]=temp
    start += 1
    end -= 1

def reverse_words(sentence):    # sentence here is an array of characters
  #reverse the array
  s_len = len(sentence)
  reverse_chars(sentence,0,s_len-1)
  temp = 0
  for i in range(1,s_len-1):
    if sentence[i]==" " and (i-1)>temp:
      reverse_chars(sentence,temp,i-1)
      temp=i+1
  reverse_chars(sentence,temp,s_len-1)
  return sentence

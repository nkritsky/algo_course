
def rotate_list(head, n):
  if n == 0:
    return head
  # get list length and store the pointer to last element
  list_len = 0
  cur = head
  while cur:
    list_len+=1
    last = cur
    cur = cur.next
  n = n % list_len
  if n < 0:
    n = list_len + n
  print ("list is {} items long, last item is {} shift {}".format(list_len,last.data,n))
  cur = head
  while n:
    cur=cur.next
    n -= 1
  last.next = head
  head = cur.next
  cur.next = None
  return head

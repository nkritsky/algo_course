def add_integers(integer1, integer2):
  result_head=None
  result_tail=None
  carry=0
  if integer1==None:
    return integer2
  elif integer2==None:
    return integer1
  while integer1 or integer2:
    carry=carry+integer1.data+integer2.data
    result_head.data=LinkedListNode(integer1.data+integer2.data)
  return integer1

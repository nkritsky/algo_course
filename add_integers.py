def add_integers(integer1, integer2):
  carry = 0
  result = None
  while integer1 or integer2:
    if integer1 == None:
      while integer2:
        sum=integer2.data + carry
        result_cur.next=LinkedListNode(sum % 10)
        result_cur=result_cur.next
        integer2=integer2.next
        carry = sum // 10
    elif integer2 == None:
      while integer1:
        sum = integer1.data + carry
        result_cur.next=LinkedListNode(sum % 10)
        result_cur=result_cur.next
        integer1=integer1.next
        carry = sum // 10
    else:
      sum = integer1.data + integer2.data + carry
      if result == None:
        result=LinkedListNode(sum % 10)
        result_cur=result
      else:
        result_cur.next=LinkedListNode(sum % 10)
        result_cur=result_cur.next
      carry = sum // 10
      integer1 = integer1.next
      integer2 = integer2.next
  if carry > 0:
    result_cur.next=LinkedListNode(carry)
      

  return result

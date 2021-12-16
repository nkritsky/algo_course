def merge_sorted(head1, head2):
  if head1==None and head2==None:
    return None
  cur1 = head1
  cur2 = head2
  if cur1.data <= cur2.data:
    result=cur1
    cur1=cur1.next
  else:
    result=cur2
    cur2=cur2.next
  cur3=result
  while cur1 or cur2:
    if cur1 == None:
      cur3.next=cur2
      return result
    elif cur2 == None:
      cur3.next=cur1
      return result
    elif cur1.data<=cur2.data:
      cur3.next=cur1
      cur1=cur1.next
      cur3=cur3.next
    else:
      cur3.next=cur2
      cur2=cur2.next
      cur3=cur3.next
  return result

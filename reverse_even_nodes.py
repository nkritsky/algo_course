def print_list(head):
  temp=head
  while temp:
    print (temp.data)
    temp=temp.next
def reverse_even_nodes(head):
  odd=head
  even=None
  while odd:
    if odd.next:
      temp=odd.next
      odd.next=odd.next.next
      temp.next=even
      even=temp
    odd=odd.next
  odd=head
  curr=head
  print("this is odd list")
  print_list(odd)
  print("this is even list")
  print_list(even)
  while odd:
    odd=odd.next
    curr.next=even
    if even:
      even=even.next
      curr=curr.next
      curr.next=odd
      curr=curr.next
  return head

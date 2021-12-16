use merge_sorted.py

def merge_sort(head):
  if head.next==None:
    return head
  if head.next.next==None:
    if head.data<=head.next.data:
      return head
    else:
      temp=head.next
      head.next=None
      temp.next=head
      return temp
  fast=head
  slow=head
  while fast:
    fast=fast.next
    if fast:
      fast=fast.next
      slow=slow.next
  fast=slow.next
  slow.next=None
  return merge_sorted(merge_sort(head), merge_sort(fast))

def reverse_k_nodes(head, k):
   new_head = None
   sub_tail = None
   prev_tail=None
   temp = None
   cur = None
   while head:
      n=k
      while n>0 and head:
         if n==k:
            sub_tail=head
            head=head.next
            temp=sub_tail
         else:
            cur=head
            head=head.next
            cur.next=temp
            temp=cur
         print ("n is {} temp is {}".format(n,temp.data))
         n-=1
      if new_head==None:
         new_head=temp
      else:
         prev_tail.next=temp
      prev_tail=sub_tail
   sub_tail.next=None
   return new_head

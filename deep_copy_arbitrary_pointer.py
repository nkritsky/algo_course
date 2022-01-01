# We are given a linked list where the node has two pointers. The first is the regular next pointer. 
# The second pointer is called arbitrary_pointer and it can point to any node in the linked list.
# Your job is to write code to make a deep copy of the given linked list. Here, deep copy means that any operations on
# the original list (inserting, modifying and removing) should not affect the copied list.

def deep_copy_arbitrary_pointer(head):
   result = None
   nodes = {}
   while head:
      if result == None:
         result=LinkedListNode(head.data)
         result_cur=result
         if head.arbitrary not in nodes:
            nodes[head.arbitrary] = LinkedListNode(head.arbitrary.data)
         result_cur.arbtrary = nodes[head.arbitrary]
      else:
         result_cur.next=LinkedListNode(head.data)
         result_cur=result_cur.next
      if head.arbitrary not in nodes:
         nodes[head.arbitrary] = LinkedListNode(head.arbitrary.data)
      result_cur.arbtrary = nodes[head.arbitrary]
      head = head.next
   return result
   

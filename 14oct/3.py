def reverse(head):


    while head :
        nex=head.next
        head.next,head.prev=head.prev,head.next
        prev=head
        head=nex



    return prev

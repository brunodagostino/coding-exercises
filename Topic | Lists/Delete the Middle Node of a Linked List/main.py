from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None or head.next == None:
        return None

    n = 0
    current = head
    while current:
        n += 1
        current = current.next

    middle = int(n / 2)
    i = 0
    current = head
    while current:
        if i == middle - 1:
            current.next = current.next.next #type: ignore

        i += 1
        current = current.next

    return head


head = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=7, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=6)))))))
new_head = deleteMiddle(head=head)
while new_head:
    if new_head.next == None:
        print(new_head.val)
    else:
        print(new_head.val, end=" -> ")

    new_head = new_head.next

head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4))))
new_head = deleteMiddle(head=head)
while new_head:
    if new_head.next == None:
        print(new_head.val)
    else:
        print(new_head.val, end=" -> ")

    new_head = new_head.next

head = ListNode(val=2, next=ListNode(val=1))
new_head = deleteMiddle(head=head)
while new_head:
    if new_head.next == None:
        print(new_head.val)
    else:
        print(new_head.val, end=" -> ")

    new_head = new_head.next
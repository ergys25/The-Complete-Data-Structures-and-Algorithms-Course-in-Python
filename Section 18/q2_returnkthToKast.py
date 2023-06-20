from LinkedList import LinkedList


def nth_to_last(l1, n):
    p1 = l1.head
    p2 = l1.head

    for i in range(n):
        if p2 is None:
            return None
        p2  = p2.next
    
    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1

custmoLL = LinkedList()
custmoLL.generate(10, 0, 99)
print(custmoLL)
print(nth_to_last(custmoLL, 3))
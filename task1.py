class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_head = None
        current = self.head
        while current is not None:
            next_node = current.next
            if sorted_head is None or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                position = sorted_head
                while position.next is not None and position.next.data <= current.data:
                    position = position.next
                current.next = position.next
                position.next = current
            current = next_node
        self.head = sorted_head

def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    tail = dummy

    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1 is not None:
        tail.next = head1
    else:
        tail.next = head2

    return dummy.next

if __name__ == "__main__":
    first_list = LinkedList()

    for value in [3, 1, 4, 2]:
        first_list.insert_at_end(value)

    print("First List:")
    first_list.print_list()

    first_list.reverse()
    print("Reversed First List:")
    first_list.print_list()

    first_list.insertion_sort()
    print("Sorted First List:")
    first_list.print_list()

    second_list = LinkedList()

    for value in [6, 5, 8, 7]:
        second_list.insert_at_end(value)

    second_list.insertion_sort()
    print("Sorted Second List:")
    second_list.print_list()

    merged_list = LinkedList()
    merged_list.head = merge_sorted_lists(
        first_list.head,
        second_list.head,
    )

    first_list.head = None
    second_list.head = None

    print("Merged List:")
    merged_list.print_list()
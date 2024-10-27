class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
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

    def sorted_insert(self, sorted_head, new_node):
        if sorted_head is None or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            sorted_head = new_node
        else:
            current = sorted_head
            while current.next is not None and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return sorted_head

    def insertion_sort(self):
        sorted_head = None
        current = self.head
        while current is not None:
            next_node = current.next
            sorted_head = self.sorted_insert(sorted_head, current)
            current = next_node
        self.head = sorted_head

    def merge_sorted_lists(self, l1, l2):
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

# Перевірка 
if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)
    print("Перший список:")
    list1.print_list()

    print("Реверсований перший список:")
    list1.reverse()
    list1.print_list()

    print("Відсортований перший список:")
    list1.insertion_sort()
    list1.print_list()

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)
    print("Другий список:")
    list2.print_list()

    print("Реверсований другий список:")
    list2.reverse()
    list2.print_list()

    print("Відсортований другий список:")
    list2.insertion_sort()
    list2.print_list()

    merged_list = LinkedList()
    merged_list.head = merged_list.merge_sorted_lists(list1.head, list2.head)
    print("Об'єднаний відсортований список:")
    merged_list.print_list()

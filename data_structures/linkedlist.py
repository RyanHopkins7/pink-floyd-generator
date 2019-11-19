#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(N) because you have to traverse the whole list"""
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) Because we saved a reference to the tail node"""
        to_append = Node(item)
        if self.head is None:
            self.head = to_append
            self.tail = self.head
        else:
            self.tail.next = to_append
            self.tail = self.tail.next

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) Because we have a reference to the head node"""
        to_prepend = Node(item)
        if self.is_empty():
            self.tail = to_prepend
        to_prepend.next = self.head
        self.head = to_prepend

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) If item at the beginning of the list
        Worst case running time: O(N) If N nodes before item"""
        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            node = node.next

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if item at the beginning of the list
        Worst case running time: O(N) if N nodes before item"""
        node = self.head

        if node is None:
            raise ValueError('Item not found in list')

        if node.data == item:
            self.head = node.next
            if self.head is None:
                self.tail = None
            return

        while node is not None:
            if node.next is not None and node.next.data == item:
                if node.next.next is not None:
                    node.next = node.next.next
                    return
                else:
                    node.next = None
                    self.tail = node
                    return
            node = node.next

        raise ValueError('Item not found in list')


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()

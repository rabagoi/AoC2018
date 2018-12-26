# Advnet of Code: Day 8
# License Metadata

# Part 1: Sum of Metadata in Tree

class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def add(self, data):
        current = self
        while current is not None:
            # Move left in the tree.
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    return
                else:
                    current = current.left
            # Move right in the tree.
            elif data > current.data:
                if current.right is None:
                    current.right = Node(data)
                    return
                else:
                    current = current.right
            else:
                print(data, "is already in the tree.")
                return

root = Node(50)
root.add(40)
root.add(60)
root.add(45)
root.add(65)
root.add(40)
print(root.left.right.data)
class nodes:
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

    def set_left_node(self, node):
        self.left_node = node

    def set_right_node(self, node):
        self.right_node = node
    
    def get_value(self):
        return self.value
    
    def print(self):
        print(self.value)
        if self.left_node:
            self.left_node.print()
        if self.right_node:
            self.right_node.print()

    def count_unival(self):
        if self.left_node is None and self.right_node is None:
            return 1
        
        if self.left_node and self.right_node:
            if self.left_node.get_value() == self.right_node.get_value():
                return self.left_node.count_unival() + self.right_node.count_unival() + 1
            else:
                return self.left_node.count_unival() + self.right_node.count_unival() + 0
        else:
            if self.left_node:
                return self.left_node.count_unival() + 0
            else:
                return self.right_node.count_unival() + 0

node1 = nodes(1)
node2 = nodes(1)
node3 = nodes(1, left_node=node1, right_node=node2)
node4 = nodes(0)
node5 = nodes(0, left_node=node3, right_node=node4)
node6 = nodes(1)

root = nodes(0, left_node=node6, right_node=node5)
print(root.count_unival())

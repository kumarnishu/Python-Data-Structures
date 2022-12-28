class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # function of adding subtree child tree node
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    # inorder traversal
    def inorder_traversal(self):
        elements = []
        # go through left subtree
        if self.left:
            elements += self.left.inorder_traversal()

        # add base node
        elements.append(self.data)
        # go through right subtree
        if self.right:
            elements += self.right.inorder_traversal()
        return elements

    # preorder traversal
    def preorder_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.preorder_traversal()
        if self.right:
            elements += self.right.preorder_traversal()
        return elements

    def postorder_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.postorder_traversal()
        if self.right:
            elements += self.right.postorder_traversal()
        return elements

    # search items in tree
    def search(self, item):
        if self.data == item:
            return True
        if item < self.data:
            # might be in left
            if self.left:
                return self.left.search(item)
            else:
                return False
        else:
            # might be in right
            if self.right:
                return self.right.search(item)
            else:
                return False

    # find minimum value
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    # find maximum value
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()


# function to build tree
def build_tree(elements):
    root = BinaryTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


# main function
if __name__ == '__main__':
    numbers = [7, 15, 14, 15, 12, 23,20, 27, 88]
    tree = build_tree(numbers)
    print(tree.inorder_traversal())
    print(tree.preorder_traversal())
    print(tree.postorder_traversal())

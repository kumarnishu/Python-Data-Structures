class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    # add child function
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    # get level of children
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    # print tree
    def print_tree(self):
        level = self.get_level()
        prefix = " " * level * 3 + "|_ _" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


# build tree
def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("macbook"))
    laptop.add_child(TreeNode("dell"))
    laptop.add_child(TreeNode("hp"))

    cell_phones = TreeNode("cell phones")
    cell_phones.add_child(TreeNode("samsung"))
    cell_phones.add_child(TreeNode("Lava"))

    tv = TreeNode("tv")
    tv.add_child(TreeNode("lg"))
    tv.add_child(TreeNode("sony"))
    tv.add_child(TreeNode("samsung"))

    root.add_child(laptop)
    root.add_child(cell_phones)
    root.add_child(tv)
    print(tv.get_level())
    return root


if __name__ == '__main__':
    tree = build_product_tree()
    tree.print_tree()
    pass

# 3 36


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    
    @staticmethod
    def parse_tuple(data):
        if isinstance(data, tuple) and len(data) == 3:
            left_sub_tree, root, right_sub_tree = data
            node = Node(root)
            node.left = BinaryTree.parse_tuple(left_sub_tree)
            node.right = BinaryTree.parse_tuple(right_sub_tree)
        elif data is None:
            node = None
        else:
            leaf_node = data
            node = Node(leaf_node)

        return node
    
    @staticmethod
    def display_tree(root, space="\t", level=0):
        if root is None:
            print(f"{space*level}\033[1;31mN\033[0m")
            return 
        
        if root.left is None and root.right is None:
            print(f"{space*level}{root.data}")
            return 
        
        BinaryTree.display_tree(root.left, level=level+1)
        print(f"{space*level}{root.data}")
        BinaryTree.display_tree(root.right, level=level+1)

        if 0 == level:
            print(f"\033[1;32mRotate the printed tree in mind clock-wise\033[0m")

r"""
        4
      /   \
    9      5
   / \    /  \
  N   6  2    4
     / \
    9   N 
"""
tree_tuple = ((None, 9, (9, 6, None)), 4, (2, 5, 4))

root = BinaryTree.parse_tuple(tree_tuple)
BinaryTree.display_tree(root)
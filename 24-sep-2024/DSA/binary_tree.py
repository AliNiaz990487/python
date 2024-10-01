
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    
r"""
        2
      /   \
     3     5 
    /    /   \
   1    3     7
         \  /  \
          4 6  8
"""

tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        left_sub_tree, root, right_sub_tree = data
        node = TreeNode(root)
        node.left = parse_tuple(left_sub_tree)
        node.right = parse_tuple(right_sub_tree)
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

def display_tree(node, space="\t", level=0):
    if node is None:
        print(f"{space*level}N")
        return 
    
    if node.left is None and node.right is None:
        print(f"{space*level}{node.key}")
        return 
    
    display_tree(node.right, level=level+1)
    print(f"{space*level}{node.key}")
    display_tree(node.left, level=level+1)
    if level==0:
        print("rotate the printed tree clock-wise in mind.")


def traverse_in_order(node):
    if node is None:
        return []
    return (traverse_in_order(node.left) + 
            [node.key] + 
            traverse_in_order(node.right))

def traverse_pre_order(node):
    if node is None:
        return []
    
    return ([node.key] + 
            traverse_pre_order(node.left) +
            traverse_pre_order(node.right))

def tree_height(node):
    if node is None:
        return 0
    
    return 1 + max(tree_height(node.left), tree_height(node.right))


def tree_size(node):
    if node is None:
        return 0

    return 1 + tree_size(node.left) + tree_size(node.right)

tree = parse_tuple(tree_tuple)
display_tree(tree)
print(traverse_in_order(tree))
print(traverse_pre_order(tree))
print(tree_height(tree))
print(tree_size(tree))


















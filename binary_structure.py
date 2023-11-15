#When the Ouput is fraction

from fractions import Fraction

class Node:
    def __init__(self, interval):
        self.interval = interval
        self.left = None
        self.right = None

def construct_cantor_set_tree(node, depth):
    if depth == 0 or node is None:
        return

    left_interval = [node.interval[0], Fraction(2 * node.interval[0] + node.interval[1], 3)]
    right_interval = [Fraction(node.interval[0] + 2 * node.interval[1], 3), node.interval[1]]

    node.left = Node(left_interval)
    node.right = Node(right_interval)

    construct_cantor_set_tree(node.left, depth - 1)
    construct_cantor_set_tree(node.right, depth - 1)

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + f"{node.interval[0]} - {node.interval[1]}")
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

def visualize_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + f"{node.interval[0]} - {node.interval[1]}")
        if node.left is not None or node.right is not None:
            visualize_tree(node.left, level + 1, "L--- ")
            visualize_tree(node.right, level + 1, "R--- ")

# Initial interval for the entire Cantor set [0, 1]
cantor_set_root = Node([Fraction(0), Fraction(1)])

# Depth determines the level of recursion, set it to control the tree depth
depth_of_tree = 3

# Construct the Cantor set binary tree
construct_cantor_set_tree(cantor_set_root, depth_of_tree)

# Print the binary tree with fractions
print_tree(cantor_set_root)


#When teh output is decimal

# class Node:
#     def __init__(self, interval):
#         self.interval = interval
#         self.left = None
#         self.right = None

# def construct_cantor_set_tree(node, depth):
#     if depth == 0 or node is None:
#         return

#     left_interval = [node.interval[0], (2 * node.interval[0] + node.interval[1]) / 3]
#     right_interval = [(node.interval[0] + 2 * node.interval[1]) / 3, node.interval[1]]

#     node.left = Node(left_interval)
#     node.right = Node(right_interval)

#     construct_cantor_set_tree(node.left, depth - 1)
#     construct_cantor_set_tree(node.right, depth - 1)

# def print_tree(node, level=0, prefix="Root: "):
#     if node is not None:
#         print(" " * (level * 4) + prefix + f"{node.interval[0]:.4f} - {node.interval[1]:.4f}")
#         if node.left is not None or node.right is not None:
#             print_tree(node.left, level + 1, "L--- ")
#             print_tree(node.right, level + 1, "R--- ")

# def visualize_tree(node, level=0, prefix="Root: "):
#     if node is not None:
#         print(" " * (level * 4) + prefix + f"{node.interval[0]:.4f} - {node.interval[1]:.4f}")
#         if node.left is not None or node.right is not None:
#             visualize_tree(node.left, level + 1, "L--- ")
#             visualize_tree(node.right, level + 1, "R--- ")

# # Initial interval for the entire Cantor set [0, 1]
# cantor_set_root = Node([0, 1])

# # Depth determines the level of recursion, set it to control the tree depth
# depth_of_tree = 3

# # Construct the Cantor set binary tree
# construct_cantor_set_tree(cantor_set_root, depth_of_tree)

# # Visualize the binary tree
# visualize_tree(cantor_set_root)

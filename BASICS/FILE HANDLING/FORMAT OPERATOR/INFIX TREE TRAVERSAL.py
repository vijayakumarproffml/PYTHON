'''

Python implementation of evaluating an expression tree using infix traversal: 

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate_expression_tree(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return int(root.value)
    
    left_val = evaluate_expression_tree(root.left)
    right_val = evaluate_expression_tree(root.right)
    
    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        if right_val == 0:
            raise ValueError("Division by zero")
        return left_val / right_val
    else:
        raise ValueError("Invalid operator")

def infix_traversal(root):
    if root:
        if root.left:
            print("(", end="")
        infix_traversal(root.left)
        print(root.value, end="")
        infix_traversal(root.right)
        if root.right:
            print(")", end="")

# Example usage:
# Creating the expression tree
root = Node('+')
root.left = Node('*')
root.right = Node('-')
root.left.left = Node('a')
root.left.right = Node('b')
root.right.left = Node('c')
root.right.right = Node('d')

# Infix traversal
print("Infix expression:", end=" ")
infix_traversal(root)

# Evaluating the expression tree
result = evaluate_expression_tree(root)
print("\nResult:", result)



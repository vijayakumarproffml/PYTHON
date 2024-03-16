class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_expression_tree(expression):
    operators = set(['+', '-', '*', '/'])
    stack = []
    
    for char in expression.split():
        print("Processing character:", char)
        if char not in operators:
            stack.append(TreeNode(char))
            print("Operand found. Stack:", stack)
        else:
            node = TreeNode(char)
            if len(stack) < 2:
                raise ValueError("Invalid expression format: not enough operands for operators.")
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
            print("Operator found. Stack:", stack)
    
    if len(stack) != 1:
        raise ValueError("Invalid expression format: too many operands.")
    
    return stack.pop()




def evaluate_expression(root):
    if root:
        if root.left and root.right:
            left_val = evaluate_expression(root.left)
            right_val = evaluate_expression(root.right)
            if root.value == '+':
                return left_val + right_val
            elif root.value == '-':
                return left_val - right_val
            elif root.value == '*':
                return left_val * right_val
            elif root.value == '/':
                return left_val / right_val
        else:
            return int(root.value)

# Example usage:
infix_expression = "3 + 4 * 5"
root = construct_expression_tree(infix_expression)
print("Infix Evaluation:", evaluate_expression(root))

prefix_expression = "+ 3 * 4 5"
root = construct_expression_tree(prefix_expression)
print("Prefix Evaluation:", evaluate_expression(root))

postfix_expression = "3 4 5 * +"
root = construct_expression_tree(postfix_expression)
print("Postfix Evaluation:", evaluate_expression(root))

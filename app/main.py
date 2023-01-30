import ast

def extract_identifiers(tree):
    identifiers = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            identifiers.append(node.id)

    return identifiers

def max_nesting_depth(node, depth=0):
    max_depth = depth
    for child in ast.iter_child_nodes(node):
        if isinstance(child, (ast.If, ast.For, ast.While, ast.FunctionDef, ast.AsyncFunctionDef)):
            child_depth = max_nesting_depth(child, depth + 1)
            max_depth = max(max_depth, child_depth)
    return max_depth

def main_method(file_path):
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())
    identifiers = extract_identifiers(tree)
    max_depth = max_nesting_depth(tree)
    
    for identifier in identifiers:
        if len(identifier) == 13:
            print(f"{identifier} has length {len(identifier)}")
            return False
        
    if max_depth > 4:
        print("too many layers")
        return False
    
    return True

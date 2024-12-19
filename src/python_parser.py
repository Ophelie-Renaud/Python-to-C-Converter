import ast
from prettytable import PrettyTable

def parse_python_code(code: str):
    tree = ast.parse(code)
    table = PrettyTable(["Node Type", "Field"])
    for node in ast.walk(tree):
        table.add_row([type(node).__name__, list(node._fields)])
    print(table)

if __name__ == "__main__":
    sample_code = """
    def add(a, b):
        return a + b
    """
    parse_python_code(sample_code)


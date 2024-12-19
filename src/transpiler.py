from src.python_parser import parse_python_code
from src.c_generator import python_to_c_function

def transpile_python_to_c(python_code: str):
    # Étape 1 : Analyser le code Python (simplifié ici)
    func_name = "add"  # Exemple statique
    args = ["a", "b"]
    body = "return a + b;"
    # Étape 2 : Générer le code C
    return python_to_c_function(func_name, args, body)

if __name__ == "__main__":
    python_code = """
    def add(a, b):
        return a + b
    """
    c_code = transpile_python_to_c(python_code)
    print(c_code)


from src.transpiler import transpile_python_to_c

def test_transpiler():
    python_code = "def add(a, b): return a + b"
    c_code = transpile_python_to_c(python_code)
    assert "void add(int a, int b)" in c_code


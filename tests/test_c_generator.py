from src.c_generator import python_to_c_function

def test_generator():
    c_code = python_to_c_function("add", ["a", "b"], "return a + b;")
    assert "void add(int a, int b)" in c_code


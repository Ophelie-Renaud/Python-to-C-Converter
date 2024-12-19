from src.python_parser import parse_python_code

def test_parser():
    sample_code = "def hello(): pass"
    assert parse_python_code(sample_code) is None  # Just checking it runs


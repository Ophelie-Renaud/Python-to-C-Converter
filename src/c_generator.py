def python_to_c_function(func_name, args, body):
    c_code = f"void {func_name}({', '.join(['int ' + arg for arg in args])}) {{\n"
    c_code += f"    {body}\n"
    c_code += "}\n"
    return c_code

if __name__ == "__main__":
    c_code = python_to_c_function("add", ["a", "b"], "return a + b;")
    print(c_code)


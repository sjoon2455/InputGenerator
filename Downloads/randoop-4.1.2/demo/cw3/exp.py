import ast
import astor

def func(a, b):
    if a>3:
        func(4, 2)
        print("ssss")

_ast = astor.code_to_ast(func)
print(ast.dump(ast.parse(_ast)))
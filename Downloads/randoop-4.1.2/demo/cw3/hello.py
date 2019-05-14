import astor

def hello():
    print('hello!')
    return

_ast = astor.code_to_ast(hello)
print(_ast.body[0].value.args[0].s)
#_ast.body[0].value.args[0].s = "arrrgh!"
exec(astor.to_source(_ast))
hello()
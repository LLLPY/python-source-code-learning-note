import dis
import py_compile

res = py_compile.compile(file='demo.py', cfile='demo.pyc')
print(res)

py_code_object = open('demo.pyc', 'rb').read()
print(py_code_object)

# bytecode: https://docs.python.org/3/library/dis.html#python-bytecode-instructions
# dis.dis(code)
dis.dis(py_code_object)

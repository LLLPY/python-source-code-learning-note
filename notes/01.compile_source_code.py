# 源码
source_code = open('demo.py').read()

# 编译成code对象(pyObjectCode)
code = compile(source_code, filename='', mode='exec')

# class code https://docs.python.org/3/reference/datamodel.html#code-objects
print(type(code))
print(code.co_code)
print(code.co_consts)
print(int.from_bytes(code.co_lnotab,byteorder='big'))
print(code.co_names)
print(code.co_varnames)


# 执行
exec(code)


# 基础对象 PyObject
"""
struct _object {
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;
    PyTypeObject *ob_type;
};
"""

# 类型对象 PyTypeObject 每一个基础对象都的结构体中都会包含这个内容，因为每一个对象它必定属于某一个类型。


#  定长对象
#  非定长对象 PyVarObject


# print(int.__base__)



# num = int(f'1{"0"*4299}')
a = 6666
print(a)
# b = 10**100
# print(b)
# c = 10**1000
# print(c)
# import sys
# sys.set_int_max_str_digits(100000)
# d = 10**10000
# print(d)

a = 1
print(a,bin(a))
b = a<< 15
print(b,bin(b))
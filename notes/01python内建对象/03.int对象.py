
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




print(int.__base__)

A = type('A',(int,),{'a':100})
a = A()
print(a.a)


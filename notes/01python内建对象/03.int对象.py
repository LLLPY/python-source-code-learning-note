
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


# d = 10**10000
# print(d)



# 为什么int是变长对象，而flaot不是？
# small_int的范围：[-5, 257]
# medium_int的范围：[-(1<<30)-1, (1<<30)-1]

# 整数对象的绝对值运算规则： The absolute value of a number is equal to ：SUM(for i=0 through abs(ob_size)-1) ob_digit[i] * 2**(SHIFT*i)
def get_value_from_ob_digit(ob_dight):
    # 偏移：移动的位数
    shift =  30
    result = 0
    for i in range(len(ob_dight)):
        result += ob_dight[i]*2**(shift*i)
    return result



a = (1<<30)-1
print('整数对象a:',a)

# 尝试转成float类型
b = float(a)
print('浮点对b:',b)

c = (1<<3100)
print('整数对象c:',c)

# d = float(c)
# print('浮点对象d:',d)

import sys
sys.set_int_max_str_digits(1000000000)
e = (1<<31000)
f = (1<<310000)
g = (1<<320000)
# print(g)


# s = '1073741823 1073741823 1073741823 1073741823 1073741823 1073741823 1073741823 1073741823 1073741823 1073741823 1'

# val = get_value_from_ob_digit(list(map(int,s.split(' '))))
# print(a,val,a==val)


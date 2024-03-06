import sys

# python虚拟机框架

def g():
    a = 10
    b = 20
    # frame对象，它是对C一级的PyFrameObject的封装
    frame = sys._getframe()
    print(f'当前的函数是:{frame.f_code.co_name} locals:{frame.f_locals} globals:{frame.f_globals}')
    caller = frame.f_back
    print(f'调用者是:{caller.f_code.co_name} locals:{caller.f_locals} globals:{caller.f_globals}')
    c = 666


def f():
    a = 'hello'
    g()


f()

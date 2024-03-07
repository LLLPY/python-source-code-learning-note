import sys


# python虚拟机框架
def get_current_frame():
    """等效于sys._getframe()"""
    try:
        1 / 0
    except:
        _, _, trace = sys.exc_info()
        return trace.tb_frame.f_back


def g():
    a = 10
    b = 20
    # frame对象，它是对C一级的PyFrameObject的封装
    frame = get_current_frame()
    print(
        f'当前的函数是:{frame.f_code.co_name} locals:{frame.f_locals} globals:{frame.f_globals} builtins:{frame.f_builtins}')
    caller = frame.f_back
    print(
        f'调用者是:{caller.f_code.co_name} locals:{caller.f_locals} globals:{caller.f_globals} builtins:{frame.f_builtins}')
    c = 666


def f():
    a = 'hello'
    g()


f()
# get_frame()

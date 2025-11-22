"""
Code adapted from: https://github.com/ptooley/numbasub/blob/master/src/numbasub/nonumba.py

Original license:
Copyright 2016 Phil Tooley

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import functools

__version__ = "1.0.0"


# https://stackoverflow.com/questions/3888158
def optional_arg_decorator(fn):
    @functools.wraps(fn)
    def wrapped_decorator(*args, **kwargs):
        # If no arguments were passed...
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            return fn(args[0])
        else:

            def real_decorator(decoratee):
                return fn(decoratee, *args, **kwargs)

            return real_decorator

    return wrapped_decorator


@optional_arg_decorator
def __noop(func, *args, **kwargs):
    return func


autojit = __noop
generated_jit = __noop
guvectorize = __noop
jit = __noop
jitclass = __noop
njit = __noop
vectorize = __noop

b1 = None
bool_ = None
boolean = None
byte = None
c16 = None
c8 = None
char = None
complex128 = None
complex64 = None
double = None
f4 = None
f8 = None
ffi = None
ffi_forced_object = None
float32 = None
float64 = None
float_ = None
i1 = None
i2 = None
i4 = None
i8 = None
int16 = None
int32 = None
int64 = None
int8 = None
int_ = None
intc = None
intp = None
long_ = None
longlong = None
none = None
short = None
u1 = None
u2 = None
u4 = None
u8 = None
uchar = None
uint = None
uint16 = None
uint32 = None
uint64 = None
uint8 = None
uintc = None
uintp = None
ulong = None
ulonglong = None
ushort = None
void = None

class X(object):
    def __init__(self):
        print("X")

class Y(object,X):
    def __init__(self):
        print("Y")

class A(object):
    def __init__(self):
        print("X")

class B(object,X):
    def __init__(self):
        print("Y")

class C(object):
    def __init__(self):
        print("X")

class D(object,X):
    def __init__(self):
        print("Y")

class E(object):
    def __init__(self):
        print("X")

class F(object,X):
    def __init__(self):
        print("Y")

class G(object):
    def __init__(self):
        print("X")

class H(object,X):
    def __init__(self):
        print("Y")

class X(object):
    def __init__(self):
        print("X")

class Y(object,X):
    def __init__(self):
        print("Y")

print(50)

class A(object):
    def __init__(self):
        print("X")

class B(object,X):
    def __init__(self):
        print("Y")


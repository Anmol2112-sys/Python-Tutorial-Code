class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 is working")


    def feature2(self):
        print("Feature 2 is working")


class B(A):

    def __init__(self):
        super().__init__()
        print("in B Init")

    def feature3(self):
        print("Feature 3 is working")


    def feature4(self):
        print("Feature 4 is working")


class C(A):
    def __init__(self):
        super().__init__()
        print("in C Init")


    def feat(self):
        super().feature2()


a1=A()

a1.feature1()
a1.feature2()


b1=B()


    
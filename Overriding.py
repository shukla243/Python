class A:

    def fun1(self):
        print('feature_1 of class A')

    def fun2(self):
        print('feature_2 of class A')


class B(A):

    def fun1(self):
        print('Modified feature_1 of class A by class B')
        #super().fun1()

    def fun3(self):
        print('feature_3 of class B')

obj = B()

obj.fun1()

obj.fun2()

obj.fun3()

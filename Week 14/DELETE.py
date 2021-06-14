class Parent(object):

    def bigSum(self, val1, val2, val3, val4):
        return val1 + val2 + val3 + val4


class Child(Parent):

    constant = 50

    def bigSum(self, *args):
        return self.constant + Parent.bigSum(self, *args)

if __name__ == '__main__':
    Parent.Child(1, 2, 3, 4, 5, 6)
    

class Restaurant(object):
    bankrupt = False
    
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")
            
            
x = Restaurant()

print x.bankrupt

y = Restaurant()

y.bankrupt = True

print y.bankrupt


print ""
print "Constructor __init__  "
print ""

class Complex():
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        
        print self.r , self.i 

a = Complex(3.0, -4.5)

print ""
print "Methods may call other methods by using method attributes of the self argument"
print ""

class Bag():
    def __init__(self):
        self.data = []
        
    def add(self, x):
        self.data.append(x)
        
    def addtwice(self, x):
        self.add(x)
        self.add(x)
        
        
b = Bag()

b.addtwice(12)
print b.data

print ""
print "@staticmethad vs  @classmethod and self"
print ""


class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x    

a=A()



print ""
print "inheritance"
print ""


class Mapping():
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


m = MappingSubclass()

print 


        
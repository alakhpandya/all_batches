"""
def avg(a, b):
    # here a & b are positional arguments
    '''Returns average of two real numbers a * b'''
    average = (a + b)/2
    return average

avg(15)     # Error
"""
# default arguments: First comes all the positional arguments & then default arguments
"""A non-default argument must not come after default argument"""
"""
def avg(a, b=20, c=30):
    print("a =", a)
    print("b =", b)
    print("c =", c)
    return (a + b + c)/3

print(avg(10))      # 20
print(avg(10, 30))  # 70/3
print(avg(20, 40, 60)) # 40

print(avg(100, c=200))
"""

# arbitrary positional arguments/ variable length arguments
"""
def avg(*args):
    # print(args)
    print(sum(args)/len(args))


# avg(10)         # 10
# avg(10, 20)     # 15
# avg(10, 20, 30) # 20
# avg()
"""
# Can we have positional, default and arbitrary arguments alltogether? Yes but their order must maintain as below:
# First comes all the positional arguments, then all default arguments and then arbitrary arguments (*args)
"""
def avg(a, *args):
    print(a)
    print(args)

avg(10)                 # 10.0
avg(10, 20)             # 15.0
avg(10, 20, 30, 40)     # 25.0
"""

def avg(a,*args):
    if args==():
        print(a)
    else:
        sum=0
        sum+=a
        for i in range(len(args)):
            sum+=args[i]
        print(sum/(len(args)+1))

# keyword arbitrary arguments:
def percentage(**kwargs):
    print(kwargs)

percentage(English=80, Physics=95, Computers=100)
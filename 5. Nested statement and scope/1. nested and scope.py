def f(x):
    print(f'x: {x}')  # convert to string
    def y(x):
        print(f'xy: {x}')  # convert to string
    y(x)

f(1)
#y(2) //NameError: name 'y' is not defined

z = 10
def f2(x):
    z = 15
    print(f'xz: {x} {z}')  # convert to string
    def y(x):
        print(f'xyz: {x} {z}')  # convert to string
    y(x)
f2(1)
print(z)

z = 10
def f3(x):
    global z
    z = 15
    print(f'xz: {x} {z}')  # convert to string
    def y(x):
        print(f'xyz: {x} {z}')  # convert to string
    y(x)
f3(1)
print(z)
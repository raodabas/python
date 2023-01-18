a=4
def b():
    a=14
    print(a)

b()
print(a)

def c():
    global a
    a=14
    print(a)

c()
print(a)
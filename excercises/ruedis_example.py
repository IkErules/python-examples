def call_me(i: int):
    print(i)

# using a default parameter works
functions = [(lambda a=i: call_me(a)) for i in range(5)]

# making a correct closure works
def make_function(i):
    return lambda: call_me(i)

functions2 = [make_function(i) for i in range(5)]


for f in functions:
    f()

for f in functions2:
    f()

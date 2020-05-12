# PCP Python Bericht
#
# Type-System
#

# Duck Typing
a = 42
b = '42'
c = '42b'
d = 42.1337

print('Type von a:',  type(a), 'Value von a:', a)
print('Type von b:', type(b), 'Value von b:', b)
print('Type von c:', type(c), 'Value von c:', c)
print('Type von d:', type(d), 'Value von d:', d)



print(type(c))
i = str(c)
print(type(c))
# PCP Python Bericht
#
# Type-System
# -------------------------------------------------------------------------------
#  Zahlen
#     ---> int, float, complex
#  Collection
#     ---> Sequenzen   ---> unveränderbar ---> str, bytestring, tuple
#                      ---> veränderbar   ---> list, bytearray
#     ---> Mengen      ---> set, frozenset
#     ---> Abbildungen ---> dict
#  Boolean             ---> bool
#  NoneType            ---> None
# -------------------------------------------------------------------------------

# Duck Typing
# Typ wird automatisch anhand der Eigenschaften evaluiert.
a = 42
print('Type von a:',  type(a), 'Value von a:', a)

a = '42'
print('Type von a:', type(a), 'Value von a:', a)

a = '42b'
print('Type von a:', type(a), 'Value von a:', a)

a = 42.1337
print('Type von a:', type(a), 'Value von a:', a)

a = int(a)
print(type(a))
a = str(a)
print(type(a))
a = int(a)
print(type(a))
print(a)

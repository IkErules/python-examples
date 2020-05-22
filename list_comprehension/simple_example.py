# PCP Python Bericht
#
# List Comprehension
#
# [dostuff(x) for x in xs if condition(x)]
#

# Imperativ ganz traditionell
x = []
for i in range (1,6):
    x.append(i * 2)
print ("Imperativ:          ", x)
# -------------------------------------------------------------

# Funktional mit Lambda
functional = list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))
print("Funktional:         ", functional)
# -------------------------------------------------------------

# List Comprehension
list_comprehension =[y * 2 for y in [1, 2, 3, 4, 5]]
print("List Comprehension: ", list_comprehension)
# -------------------------------------------------------------

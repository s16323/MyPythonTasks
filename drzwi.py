sample_list = [1,2,3,4,5,6,7,8,9,10]


coriddor = [0 for x in range(0, 100)]           # listo of 100 zeros

print(coriddor)
print(coriddor[0])
print(coriddor.count(0))         # gives number of occurances of an element
print(len(coriddor))             # gives length of a list


# # first visiting:
a = 1
n = a
while n <= 100:
    if coriddor[n] == 0:
        coriddor[n] = 1
    else:
        coriddor[n] = 0
    n += (a+1)

print(coriddor)

# # second visiting:
a = 2
n = a
while n <= 100:
    if coriddor[n] == 0:
        coriddor[n] = 1
    else:
        coriddor[n] = 0
    n += (a+1)

print(coriddor)

# third visiting:
a = 3
n = a
while n <= 100:
    if coriddor[n] == 0:
        coriddor[n] = 1
    else:
        coriddor[n] = 0
    n += (a+1)

print(coriddor)












# enum = enumerate(coriddor)
# print(next(enum))



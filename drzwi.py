
coriddor = [0 for x in range(0, 100)]           # listo of 100 zeros

print(coriddor)
# print(coriddor[0])
print(coriddor.count(0), 'closed doors in corridor.')         # gives number of occurrences of an element
print(len(coriddor), 'total doors in corridor.')              # gives length of a list


for a in range(1, 100):
    print(a, 'visiting')
    n = a
    while n <= 100:
        if coriddor[n] == 0:
            coriddor[n] = 1
            print('opened', n, 'door')
        else:
            coriddor[n] = 0
            print('closed', n, 'door')
        n += (a+1)


print('\n---------Outcome:---------\n')
print('current corridor state:\n', coriddor)
print(coriddor.count(1), 'open doors in the corridor.')
print(coriddor.count(0), 'closed doors in the corridor.')
# enum = enumerate(coriddor)
# print(next(enum))





# # # first visiting:
# a = 1
# n = a
# while n <= 100:
#     if coriddor[n] == 0:
#         coriddor[n] = 1
#     else:
#         coriddor[n] = 0
#     n += (a+1)
#
# print(coriddor)
#
# # # second visiting:
# a = 2
# n = a
# while n <= 100:
#     if coriddor[n] == 0:
#         coriddor[n] = 1
#     else:
#         coriddor[n] = 0
#     n += (a+1)
#
# print(coriddor)
#
# # third visiting:
# a = 3
# n = a
# while n <= 100:
#     if coriddor[n] == 0:
#         coriddor[n] = 1
#     else:
#         coriddor[n] = 0
#     n += (a+1)






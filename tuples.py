t1 = (1, 'two', 3)
print(t1)

t2 = (t1, 'four')
print(t2)

#concatonation
print t1 + t2

#indexing
print((t1 + t2)[3])

#slicing
print (t1 + t2)[2:5]

#singletons
t3 = ('five',)
print t1 + t2 + t3

#iterations
def oddTuples(aTup):
    bTup = ()
    for i in range(len(aTup)):
        if i%2 == 0:
            bTup = bTup + (aTup[i],)
    return bTup



aTup = ('I', 'am', 'a', 'test', 'tuple')
print oddTuples(aTup)


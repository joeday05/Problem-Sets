## universities

Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]

Techs.append('RPI')   #mutates existing list Techs....Univs1 does not mutate

print('Univs = ')
print(Univs)
print('')
print('Univs1 =')
print(Univs1)


for e in Univs:
    print('Univs contains ')
    print(e)
    print('   which contains')
    for u in e:
        print('      ' + u)




class Test:
    data = []   #mutable typ

    def __init__(self):
        self.o_date = 0


print('\nclass attribute\'s behavior in python\n')

t1 = Test()
t2 = Test()
print('instances')
print(t1.data)
print(t2.data)
print('class: ')
print(Test.data)

print('\nMODIFICATION (accessing through 1st instance) ')
t1.data.append(1)
print('instances')
print(t1.data)
print(t2.data)
print('class: ')
print(Test.data)

print('\nMODIFICATION (accessing through 2nd instance) ')
t2.data.append(2)
print('instances')
print(t1.data)
print(t2.data)
print('class: ')
print(Test.data)

print('\nMODIFICATION (accessing through class)')
Test.data.append(100)
print('instances')
print(t1.data)
print(t2.data)
print('class: ')
print(Test.data)

print('\nASSIGNMENT (accessing through class)')
Test.data = [99, 98, 97]
print('instances')
print(t1.data)
print(t2.data)
print('class: ')
print(Test.data)

print('\nASSIGNMENT (accessing through 1st instance)')
t1.data = [999, 998, 997]
print('instances')
print(t1.data)
print(t2.data)
print('class: ')
print(Test.data)

print('\nASSIGNMENT (accessing through class, again!)')
Test.data = [0, 0, 0]
print('instances')
print(t1.data)
print(t2.data)
print('class: ')
print(Test.data)

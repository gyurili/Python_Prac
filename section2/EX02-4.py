'''튜플'''

t = (1, 2, 3)
print(t)

print('---------------')

'''세트'''

s = {1,1,2}
s.add(40)
s.remove(1)
print(s)

s = list(set([1,1,2]))
print(s)

print('---------------')

'''딕셔너리'''

d = {'a':'apple', 'b':'banana'}
d['w'] = 'water'
d.update(a='air')
d.update(c='car')
d.pop('b')
print(d)
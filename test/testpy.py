# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)
#
# person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# from collections import Iterable
# list = [x*x for x in range(1, 11) if x%2==0]
# print(list)
# import os
# print([d for d in os.listdir('.')])
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# print([k + '=' + v for k, v in d.items()])
#
# g = (x * x for x in range(10))
# for n in g:
#     print(n)


from collections import Iterator
print(isinstance(iter('abc'), Iterator))
# 아이디 연산자(Identity Operators)
a = 10
b = 10
c = 11
print(a, 'id =', id(a))
print(b, 'id =', id(b))
print(c, 'id =', id(c))
print('같은 객체' if a is b else '다른 객체')
print('같은 객체' if a is c else '다른 객체')
print('다른 객체' if a is not c else '같은 객체')
print()

name1 = '한사람'
name2 = '한사람'
name3 = '두사람'
print(name1, 'id =', id(name1))
print(name2, 'id =', id(name2))
print(name3, 'id =', id(name3))
print('같은 객체' if name1 is name2 else '다른 객체')
print('같은 객체' if name1 is name3 else '다른 객체')
print('다른 객체' if name1 is not name3 else '같은 객체')
print()

name4 = name3
print(name3, 'id =', id(name3))
print(name4, 'id =', id(name4))
print('같은 객체' if name3 is name4 else '다른  객체')
print()

name3 = '세사람'
print(name3, 'id =', id(name3))
print(name4, 'id =', id(name4))
print('같은 객체' if name3 is name4 else '다른  객체')
print()
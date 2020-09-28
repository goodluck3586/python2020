# 딕셔너리 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a)  # {1: 'a', 2: 'b'}

a['name'] = 'dongyun'
print(a)  # {1: 'a', 2: 'b', 'name': 'dongyun'}

a[3] = [1,2,3]
print(a)  # {1: 'a', 2: 'b', 'name': 'dongyun', 3: [1, 2, 3]}

# key값으로 value값 가져오기
print(a[1], a['name'], a[3])  # a dongyun [1, 2, 3]

#region 딕셔너리 함수
print(a.keys())  # dict_keys([1, 2, 'name', 3])

for k in a.keys():
    print(k, end=' ')  # 1 2 name 3
print()
print(list(a.keys()))  # [1, 2, 'name', 3]

print(a.values())  # dict_values(['a', 'b', 'dongyun', [1, 2, 3]])

# key, value값 쌍으로 가져오기
print(a.items())  # dict_items([(1, 'a'), (2, 'b'), ('name', 'dongyun'), (3, [1, 2, 3])])

# 모두 지우기
a.clear()
print(a)  # {}

# key값으로 value값 얻기
print(a.get('name'))  # None



#endregion



# a, b = input().split()
# print(b, a)

# n = float(input())
# print("%.2f" %n)

# n = int(input())
# print('%d %d %d'%(n,n,n))

# date = input().split('.')
# print('%04d.%02d.%02d'%(int(date[0]), int(date[1]), int(date[2])))

# n = input().replace('-','')
# print(n)

# w = input().split('.')
# print(w[0])
# print(w[1])

# w = input()
# for i in w:
#     print("'%c'"%i)

# i = input()
# i_len = pow(10, len(i)-1)

# # print(i_len)
# numList = []
# for val in i:
#     numList.append(int(val))

# for val in numList:
#     print('[{0}]'.format(val * i_len))
#     i_len = int(i_len/10)

# i = input().split(':')
# print(int(i[1]))

# date = input().split('.')
# print('%02d-%02d-%04d'%(int(date[2]), int(date[1]), int(date[0])))

# i = float(input())
# print('%.11f'% i)

# i = int(input())
# # print(format(i, 'o'))
# print(str(format(i, 'x')).upper())

# i = input()
# i = '0o' + i
# print(int(i, 10))


i = input()
l = len(i)  # 길이
print(pow(8, l-1))
i = int(i)

while True:
    if l<0:
        break
    pow(8, l)


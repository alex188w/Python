
# with open('test_file.txt', encoding='utf-8') as file:
#     for line in file.read():
#         print(line)
    #print(line.decode(encoding='utf-8'))


# a = b'\xef\xff\xf2\xfc'
# c = bytes.decode(a, encoding='utf-8')
# print(c)

file = open('test_file.txt', 'rb')
for line in file:
    print(line)
    print(line.decode(encoding))
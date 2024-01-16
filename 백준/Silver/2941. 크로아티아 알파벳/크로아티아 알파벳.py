string = input()
datas = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for data in datas:
    string = string.replace(data, "*")
print(len(string))
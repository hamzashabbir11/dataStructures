old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9
print(new_list)
print(id(new_list))
print(id(old_list))

print(new_list)
print(old_list)

A=new_list.copy()
print(A)
print(id(A))


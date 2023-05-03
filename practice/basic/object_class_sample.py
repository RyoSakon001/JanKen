a = 100
b = 100
print(a == b, a is b, id(a), id(b)) # idはメモリ上のアドレスを返す。今回はアドレスが同じ

list1 = [1, 2, 3]
list2 = [1, 2, 3]
# idはメモリ上のアドレスを返す。今回はアドレスが異なる
print(list1 == list2, list1 is list2, id(list1), id(list2))
list1[0] = 4
print(list1, id(list1)) # リストの要素を変更してもアドレスは変わらない
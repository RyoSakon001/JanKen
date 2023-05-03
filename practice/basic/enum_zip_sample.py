# enumrate型: インデックス番号と要素を同時に取得できる
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(type(enumerate(seasons))) # <class 'enumerate'>
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=5 )))

english = 'English'
print(list(enumerate(english, start=1)))
for (i, c) in enumerate(english):
    print(i, c)

dic = {'a': 1, 'b': 2, 'c': 3}
print(list(enumerate(dic))) # keyを取得する
for (i, key) in enumerate(dic, start=101):
    print(i, key)

products = ['T-shirt', 'Sweater', 'Jeans']
prices = [3000, 5000, 8000]
quantities = [1, 2, 3]
buys = list(zip(products, prices, quantities)) # zip: 複数のリストをtupleにまとめる
# もし、リストの要素数が異なる場合は、最小の要素数に合わせる
print(buys, type(buys[0]))
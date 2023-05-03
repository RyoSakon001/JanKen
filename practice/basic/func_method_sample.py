"""関数（ファンクション）とメソッドの違い
関数: 引数を受け取り、returnで値を返す。何も返さない場合はNoneが返却される
メソッド: モジュールやクラスに属している関数。オブジェクトに対して実行する
"""


x = print(1)
print(x) # return値がないのでNoneが入る

def add1(a, b):
  return a + b
def add2(a, b=100):
  return a + b

print(add1(10, 5))
print(add2(10))

print('swimming'.count('m')) # これはオブジェクトに対して実行するのでメソッド
numbers = [1, 2, 3]
numbers.append(4) # これもメソッド
print(numbers)
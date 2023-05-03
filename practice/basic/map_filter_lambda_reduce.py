# map型: listに対して関数を適用する
# Iterable型: list, tuple, dict, set, str, bytes, range, map, filter → for文で繰り返し処理ができる
nums = map(int, ['1', '2', '3']) # intに括弧をつけると実行されてしまいエラーになる
print(nums, type(nums)) # map型
for num in nums:
    print(num)
print(nums) # 一度実行すると空になる

# filter型: Iterable型の要素に関数を適用し、Trueのものだけを取り出す
def is_even(x):
    return x % 2 == 0

nums_filter = map(int, ['1', '2', '3', '4', '5', '6'])
evens_filter = filter(is_even, nums_filter)
print(evens_filter, type(evens_filter)) # そのままでは使えない
print(list(evens_filter)) # listに変換すると使える

# lambda式: 無名関数。一度しか使わない関数を定義するときに使う
nums_lambda = map(int, ['1', '2', '3', '4', '5', '6'])
evens_lambda = filter(lambda x: x % 2 == 0, nums_lambda)
print(list(evens_lambda))

# reduce関数: Iterable型の要素に関数を適用し、結果を累積していく
from functools import reduce
result = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]) # 1*2=2, 2*3=6, 6*4=24, 24*5=120
print(result)
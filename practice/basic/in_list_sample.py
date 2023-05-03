# リスト内包表記
nums = [x for x in range(10)] # xに0から9までの値を代入
squares = [x*x for x in range(10)]
doubles = [x if x % 2 == 0 else x * 2 for x in range(10)] # 三項演算子
ages = [str(x) + '歳' for x in range(10)]
print(nums)
print(squares)
print(ages)
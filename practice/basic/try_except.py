nums = [0, 1, 2]
try:
    # print(nums[3])
    a = 1 / 0

except IndexError as e:
    print(e)
    print(type(e))  # エラーの実態はインスタンス
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print('どんなエラーでもここにくる')

print('Done!')
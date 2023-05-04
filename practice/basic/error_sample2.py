# 独自例外クラス
class TemperatureError(Exception):
    pass

try:
    body_temp = float(input('体温を入力してください: '))
except ValueError:
    print('体温は数値で入力してください')
    exit()

if body_temp < 35.0 or body_temp > 42.0:
    raise TemperatureError('体温が正常値の範囲を超えています')
elif body_temp >= 37.5:
    print('コロナの可能性があります')
else:
    print('コロナの可能性は低いです')
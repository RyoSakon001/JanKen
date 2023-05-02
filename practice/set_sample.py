# 集合型
hands = {'グー', 'チョキ', 'チョキ', 'グー', 'チョキ'}
print(hands, type(hands))
hands.add('パー') # どの位置に追加されるかは不定
print(hands)
# print(hands[0]) # エラー
print(list(hands)[0]) # リストに変換してからインデックス指定ならOK

"""
discard()は、指定した要素が存在しない場合は何もしない
remove()は、指定した要素が存在しない場合はエラーになる
"""
hands.discard('チョキ')

print(hands)

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b) # 和集合
print(a & b) # 積集合
print(a - b) # 差集合
print(a ^ b) # 重複した要素を取り除いた集合
hand_types = ['グー', 'チョキ', 'パー']
n = int(input('じゃんけんをする人数を入力してください: '))

hands = []
while len(set(hands)) != 2:  # 手が2種類ならば、あいこにならない
    for i in range(n):
        hands.append(int(input(str(n) + '人目の手を入力してください。（0: {} 1: {} 2: {}） : ' .format(*hand_types))))

    if set(hands) - {0, 1, 2} != {}:
        print('0, 1, 2のいずれかを入力してください')
        hands = []
        continue

    if len(set(hands)) != 2:
        print('あいこです。もう一度入力してください')
        hands = []
        continue

if 0 not in set(hands):
    print('1: ' + hand_types[1] + 'を出した人が勝ちです')
elif 1 not in set(hands):
    print('2: ' + hand_types[2] + 'を出した人が勝ちです')
else:
    print('0: ' + hand_types[0] + 'を出した人が勝ちです')

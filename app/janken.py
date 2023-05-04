class Janken:
    hand_types = ['グー', 'チョキ', 'パー']

    def play(self):
        hands = []
        n = int(input('じゃんけんをする人数を入力してください>>>'))

        while True:
            for i in range(n):
                hands.append(
                    int(input(str(i + 1) + '人目の手を入力してください。（0: {} 1: {} 2: {}）\n>>>' .format(*Janken.hand_types))))  # *は、リストの中身を展開して渡す

            if self.validate(hands):
                print('0, 1, 2のいずれかを入力してください')
                hands = []
                continue

            print(self.hands_text(hands))

            if self.is_aiko(hands):
                print('あいこです。もう一度入力してください')
                hands = []
            else:
                break
        print(self.result(hands))

    def is_aiko(self, hands):  # 手が2種類ならば、あいこにならない
        return len(set(hands)) != 2

    def validate(self, hands):
        return set(hands) - {0, 1, 2} != set()

    def hands_text(self, hands):
        text = ''
        for i, hand in enumerate(hands):
            text += str(i + 1) + '人目: ' + Janken.hand_types[hand] + ' '
        return text

    def result(self, hands):
        if 0 not in set(hands):
            win = '1: ' + Janken.hand_types[1]
        elif 1 not in set(hands):
            win = '2: ' + Janken.hand_types[2]
        else:
            win = '0: ' + Janken.hand_types[0]
        return win + 'を出した人が勝ちです'

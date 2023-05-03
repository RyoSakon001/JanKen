class Fish:
    # インスタンスの作り方
    pass


funa = Fish()
nijimasu = Fish()
print(type(funa))  # <class '__main__.Fish'> mainは、このファイルに属するモジュールのクラスという意味
print(type(nijimasu))
print(funa == nijimasu, funa is nijimasu)


class Animal:

    count = 0  # クラス変数

    def __init__(self, kind, age):  # コンストラクタ
        print('私は動物です。インスタンスを定義したので、__init__関数が実行されます。')
        self.kind = kind  # 例: poshi.kind = '犬'
        self.age = str(age) + '歳'  # 例: poshi.age = '5歳'
        Animal.count += 1

    # クラスメソッドではなく、インスタンスメソッド。ドットでつなげて呼び出すため、関数ではなくメソッドと呼ぶ
    def cry(self, voice):
        print('私は' + self.kind + 'です。' + voice)


pochi = Animal('犬', 5)  # self以降の引数を渡す
# インスタンスに紐づけるのか、クラスに紐づけるのか注意する
print(pochi.kind, pochi.age, str(Animal.count) + '匹目')
tama = Animal('猫', 3)
print(tama.kind, tama.age, str(Animal.count) + '匹目')

pochi.cry('わんわん！')
tama.cry('にゃにゃーご！')


class Dog(Animal):  # 継承
    def run(self):
        print('散歩が大好きです。')


shiro = Dog('しば犬', 10)
shiro.cry('わおーん！')

# poshi.run()  # エラーになる
shiro.run()


class Cat(Animal):
    def __init__(self, kind, age, color):
        super().__init__(kind, age)  # 親クラスのコンストラクタを呼び出す
        self.color = color
        print(str(color)+'の'+str(kind) +
              'だにゃん！superでAnimalのコンストラクタを呼び出したから、colorだけ追加できるにゃん！')

    def cry(self):
        print('Animalのcryをオーバーライドしたから、新しい内容で鳴くにゃん！')


mike = Cat('三毛猫', 2, 'white')
mike.cry()

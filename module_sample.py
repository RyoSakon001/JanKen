"""
モジュール: Pythonでは、関数や変数、クラスをファイルにまとめたもの（ライブラリ）
importで読み込んで使う
"""

import random # これがモジュールの読み込み
lang = ['Python', 'Ruby', 'PHP', 'Java', 'JavaScript', 'Go', 'C', 'C++', 'Swift']
random.shuffle(lang) # 「random」というモジュールの「shuffle」という関数を使う
print(lang)
print(random.choice(lang))

from math import floor, ceil # fromを使うとモジュール名を省略できる
x = 3.14
print(floor(x)) # 小数点以下切り捨て
print(ceil(x)) # 小数点以下切り上げ

import sys
sys.path.append('/modules') # モジュールの検索パスを追加
from modules import calculator
print(calculator.calc_add(1000, 234))
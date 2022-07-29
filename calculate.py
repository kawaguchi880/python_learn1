# 四則演算
from random import sample
from re import S


print('<四則演算>')
print(10+2)
print(10-2)
print(10*10)
print(10 % 4)
print('----------------------')
# pythonでは配列はlistという
sampleList = [10, 20, 30]
print(type(sampleList))

sampleDictionary = {}
print(type(sampleDictionary))

sampleTuple = ()
print(type(sampleTuple))
print('------------------------')
print('<listについて>')
list = []

names = ['今西', '鈴木', '佐藤']

print(names[-3])

# [0:2]は0から1までのindex値を取る
print(names[0:2])

# すべて取る
print(names)

# index値1以降をすべて取る
print(names[1:])

scores = [40, 20, 30, 50]

print(scores)
# .append()でlistに後ろに追加する
scores.append(100)
print(scores)
# .pop()でlistの最後を消す
scores.pop()
print(scores)
# pop関数内にindex値を指定することでそこが消える．
scores.pop(0)
print(scores)

# ほかにも，clear()やremove(),del文などでも消せる．詳細はREADME.mdに記載しておく．

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del l[2:8:2]
print(l)

# 辞書について
print('---------------------')
print('< 辞書について > ')
scores = {'国語': 40,
          '数学': 90,
          '英語': 80,
          '理科': 80,
          '社会': 70}

print(scores['国語'])
# 値の追加
scores['家庭科'] = 10
# 値の削除
scores.pop('数学')
print(scores)

print('-------------------')
print('<if文について>')

money = 100

if money >= 8000:
    print('ディズニーランドに行ける')
elif money >= 2000:
    print('映画に行ける')
else:
    print('映画にいけない')

print('---------------')
print('for文について')

for i in range(len(names)):
    print(names[i] + 'さん')
# range()で関数内の数文forを回す
# len()で関数内の要素数になる

for name in names:
    print(name + 'さん')
print('---------------------------')
print('zip関数とenumerate関数について')
# zip は複数のlistの要素をまとめて処理したい
first_names = ['今田', '近藤', '川口', '岡田']
last_names = ['綾瀬', '紗綾', '春樹', '緑']
full_names = []
for last_names, first_names in zip(last_names, first_names):
    full_name = first_names + last_names
    full_names.append(full_name)
print(full_names)

# enumerate
last_names = ['綾瀬', '紗綾', '春樹', '緑']
print(last_names)
for i, last_name in enumerate(last_names):
    print(f'出席番号{i}番目の{last_name}さん')

# 関数について

name1 = 'かかし'


def say_hello(name):
    print(f'{name}さんこんにちは！')


say_hello(name1)
# クラス


class Person:
    def __init__(self, name, nationality, age) -> None:
        self.name = name
        self.nationality = nationality
        self.age = age

    def say_hello(self):
        print(f'{self.name}さん，こんにちは！')

    def __call__(self, name):
        print(f'{name}さん，こんにちは私は{self.name}です．')


kawaguchi = Person(name='川口', nationality='日本', age=20)
kawaguchi.say_hello()
kawaguchi(name='imamiya')

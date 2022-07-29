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

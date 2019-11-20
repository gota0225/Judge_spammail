#メール内の文字の出てくる頻度を調べる
import sys
import MeCab

file = sys.argv[1]
m = MeCab.Tagger("-Owakati")
with open(file, "r") as fp:
    wordlists = []
    for line in fp:
        words = m.parse(line)
        keyslists = []
        for word in words:
            keyslists.append(word)
        wordlists.append(keyslists)

dic_words = {}
i = 0
for list in wordlists:
    print(list[0])
    break



import sys
import MeCab

m = MeCab.Tagger("-Owakati")
word_dic = {}
file = sys.argv[1]
with open(file, 'r') as fp:
    word_count = 0
    for line in fp:
        line = line.rstrip()
        words = m.parse(line)
        wordArray = words.split()

        word_count += len(wordArray)

print(word_count)
print(words)
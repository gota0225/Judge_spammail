#スパムメールとノットスパムメールを分けてその数を表示する
import sys
file = sys.argv[1]
with open(file, "r") as fp:
    dic_lists = []
    for line in fp:
        dic_lists.append(line[0])

dic_value = []
dic_f = {}
for word in dic_lists:
    if dic_f.get(word) == None:
        dic_f[word] = 1
        str1 = word
    if dic_lists[0] == word:
        dic_f[word] = 0
    value = int(dic_f[word])
    dic_value.append(value)

con_s = dic_value.count(1)
con_n = dic_value.count(0)
print(str1, con_s)
print(dic_lists[0], con_n)

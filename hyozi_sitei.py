import sys
file = sys.argv[1]
with open(file, 'r') as fp:
    lines = []
    for line in fp:
        line = line.rstrip()
        lines.append(line)

n_number = int(sys.argv[2])
m_number = int(sys.argv[3])
if n_number <= m_number:
    print(lines[n_number-1:m_number])
else:
    print('error')
